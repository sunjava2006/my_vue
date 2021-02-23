from flask import Flask, request, make_response, jsonify, render_template, session, redirect
from db.dbaccess import Admin, Types, Fruits
import random
import datetime
from flask_cors import CORS



app = Flask(__name__)
app.secret_key = "123456789"
# cors = CORS(app, support_credentials=True)

# 设置session有效时间
app.permanent_session_lifetime = datetime.timedelta(minutes=61)

@app.before_request
def before():
    print(request.headers)
    print("*" * 100)
    host = request.headers.get("Host")
    if host != 'wr.free.idcfengye.com':
        if "login" not in request.path:
            if not session.get("user_info"):
                response = make_response("", 200, {"session-status": "invalide"})
                return response

@app.after_request
def after(res):
    print("res: ", res, res.headers)
    if session.get("user_info"):
        res.headers["session-status"] = "valide"
    else:
        res.headers["session-status"] = "invalide"
    return res

@app.route("/login")
def login():
    userName = request.args.get("userName")  # request.args["userName"] args属性仅用于get方法获取参数
    pwd = request.values.get("pwd")  # values可用在get、post请求中获取参数。

    print(userName, pwd)
    admin = Admin()
    user = admin.login(userName, pwd)
    admin.close()

    if user:
        session["user_info"] = user
        session.permanent = True
        print(session)

    if user:
        return jsonify({"login": "ok", "userInfo": user})
    else:
        return jsonify({"login": "nook"}), 200  # 内容，状态码，响应头


@app.route("/login.html", methods=["GET"])
def loginpage():
    return render_template("/login.html")





@app.errorhandler(404)
def err404(err):
    return render_template("/404.html")


@app.route("/addType", methods=["POST", "GET"])
def addType():
    # type = request.form.get("type")  # 获取 post方式发类的请求参数
    type = request.values.get("type")  # values 可以获取 get \post 发送的参数

    types = Types()
    if types.have_type(type):  # 查询数据库中是否已经有存在的类型
        types.close()
        return "repeat", 200, {"Access-Control-Allow-Origin": "*"}
    else:
        types.add_type(type)
        types.close()
        return "ok", 200, {"Access-Control-Allow-Origin": "*"}

@app.route("/listTypes", methods=["POST", "GET"])
def listTypes():
    user_info = session.get("user_info")
    print("user_info", user_info)
    if user_info:
        page = request.values.get("page")
        size = request.values.get("size")
        print(request.values)
        types = Types()
        typeList = types.list(int(page), int(size))
        total_count = types.total_count()
        total_page = types.total_page(total_count, int(size))
        types.close()
        data = {"typeList": typeList, "totalPage": total_page, "totalCount": total_count, "currentPage": int(page)}

        return jsonify(data), 200
    else:
        # response = make_response()
        # return jsonify(None), 200, {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Credentials": "true"}
        return "", 200

@app.route("/modifyType")
def modifyTpye():
    type = request.args.get("type")
    id = int(request.args.get("id"))
    types = Types()
    if types.have_type(type):
        types.close()
        return "repeat", 200
    else:
        count = types.modify_type(type, id)
        types.close()
        if count == 1:
            return "ok", 200
        else:
            return "nook", 200


@app.route("/delType")
def delType():
    id = int(request.values.get("id"))

    # 查询该类型是否已经被引用
    fruits = Fruits()
    if fruits.type_count(id):
        fruits.close()
        return "used", 200
    else:
        types = Types()
        types.del_type(id)
        types.close()
        return "ok", 200


@app.route("/getTypeList")
def getTypeList():
    types = Types()
    data = types.list_all()
    return jsonify(data), 200


@app.route("/addFruit", methods=["POST"])
def addFruit():
    try:
        fruitName = request.values.get("fruitName")
        typeID = request.values.get("typeID")
        origion = request.values.get("origion")
        unit = request.values.get("unit")
        price = request.values.get("price")
        photo = request.files.get('photo')

        photoName = photo.filename
        dotAt = photoName.rfind(".")
        suffix = photoName[dotAt::]
        newName = str(round(random.random()*1000000000000000))+suffix
        path = "D:/_git_code_workspace/202004/py/fruit/fruitserver/static/"
        photo.save(path+newName)  # 保存文件

        # 存储到数据库
        fruits = Fruits()
        fruits.add(fruitName, typeID, price, origion, unit, newName)
        fruits.close()

        return "ok", 200

    except Exception as ex:
        print(ex)
        return "nook", 200

@app.route("/searchFruit")
def serarchFruit():
    page = int(request.args.get("page"))
    size = int(request.args.get("size"))
    search_type = request.args.get("searchType")
    search_key = request.args.get("searchKey")

    fruits = Fruits()
    fruit_list = fruits.search_fruit(page, size, search_type, search_key)
    total_count = fruits.search_fruit_count(search_type, search_key)
    total_page = fruits.total_page(total_count, size)
    fruits.close()

    data = {"fruitList": fruit_list, "totalCount": total_count, "totalPage": total_page, "currentPage": page}
    return jsonify(data), 200


@app.route("/listFruitByType", methods=["POST", "GET"])
def list_fruit_by_type():
    page = int(request.values.get("page"))
    type_id = int(request.values.get("typeID"))
    fruits = Fruits()
    fruit_list = fruits.list_by_type_id(type_id, page)
    total_count = fruits.count_by_type_id(type_id)
    total_page = fruits.total_page(total_count, 10)
    data = {"fruitList": fruit_list, "totalCount": total_count, "totalPage": total_page, "currentPage": page}
    return jsonify(data), 200


@app.route("/logout")
def logout():
    print('===================logout==================')
    session.clear()
    return jsonify({"logout": "ok"})


if __name__ == "__main__":
    app.run(debug=True)




