from tkinter import *
import tkinter.messagebox
import requests
import json
from functools import partial
import PIL
from PIL import ImageTk,Image
import webbrowser



def dquit():
    answer=tkinter.messagebox.askokcancel("WARNING!!!",
        "Are you sure you want to exit")
    if(answer):
        quit()
root=Tk()

api_key = '5YoVtLHoCqewYcyy1LG2syeBxORhyK4wd1s'
url_categories = 'https://price-api.datayuge.com/api/v1/compare/list/categories'
url_search = "https://price-api.datayuge.com/api/v1/compare/search"
url_detail = "https://price-api.datayuge.com/api/v1/compare/detail"





def detailp(p):
    root2=Tk()
    root2.geometry("1000x1000")
    querystring = {"api_key": api_key, "product": p}
    headers = {'content-type': 'application/json'}

    response_search1 = requests.request("GET", url_search, headers=headers, params=querystring)
    # res_sear_json = response_search.text.read()
    res_sear_json_temp = json.loads(response_search1.text)

    for j in range(len(res_sear_json_temp['data'])):
        if res_sear_json_temp['data'][j]['product_title'] == p:
            pro_name = p
            pro_id = res_sear_json_temp['data'][j]['product_id']
            pro_category = res_sear_json_temp['data'][j]['product_category']
            pro_rating = res_sear_json_temp['data'][j]['product_rating']

    querystring_pro = {"api_key": api_key, "id": pro_id}
    response_detail1 = requests.request("GET", url_detail, headers=headers, params=querystring_pro)

    res_det_json = json.loads(response_detail1.text)

    detail_dict = res_det_json['data']['stores']

    amazon_dict = detail_dict[0]
    flipkart_dict = detail_dict[1]
    croma_dict = detail_dict[5]
    infibeam_dict = detail_dict[10]
    tatacliq_dict = detail_dict[11]
    shopclues_dict = detail_dict[12]


    name1 = Label(root2, text = res_det_json['data']['product_name'], fg = 'black', font = ('fixedsys', 34))
    name1.pack()
    name2 = Label(root2, text = 'Rating: ' + res_det_json['data']['product_ratings'], fg = 'yellow', font = ('system', 28))
    name2.pack()
    empty = Label(root2, text =" ")
    empty.pack()


    try:
        str="Amazon: Rs."
        str=str+amazon_dict['amazon']['product_price']
        l1 = Label(root2, text=str,fg="red", bg = 'white', font = ('arial', 20))
        l1.pack()


    except:
        str="Amazon: Sorry! Item not available"
        l1 = Label(root2, text=str, fg="red", bg='white', font=('arial', 20))
        l1.pack()


    try:
        str = "Flipkart: Rs."
        str = str + flipkart_dict['flipkart']['product_price']
        l1 = Label(root2, text=str, fg="BLUE", bg = 'yellow', font = ('arial', 20))
        l1.pack()

    except:
        str = "Flipkart: Sorry! Item not available"
        l1 = Label(root2, text=str, fg="BLUE", bg='yellow', font=('arial', 20))
        l1.pack()


    try:
        str = "Croma: Rs."
        str = str + croma_dict['croma']['product_price']
        l1 = Label(root2, text=str, fg="GREEN", bg = 'white', font = ('arial', 20))
        l1.pack()

    except:
        str = "Croma: Sorry! Item not available"
        l1 = Label(root2, text=str, fg="GREEN", bg='white', font=('arial', 20))
        l1.pack()

    try:
        str = "Infibeam: Rs."
        str = str + infibeam_dict['infibeam']['product_price']
        l1 = Label(root2, text=str, fg="BLACK", bg = 'orange', font = ('arial', 20))
        l1.pack()

    except:
        str = "Infibeam: Sorry! Item not available"
        l1 = Label(root2, text=str, fg="BLACK", bg='orange', font=('arial', 20))
        l1.pack()

    try:
        str="TataCliq: Rs."
        str=str+tatacliq_dict['tatacliq']['product_price']
        l1 = Label(root2, text=str,fg="ORANGE", bg = 'black', font = ('arial', 20))
        l1.pack()

    except:
        str = "TataCliq: Sorry! Item not available"
        l1 = Label(root2, text=str, fg="ORANGE", bg='black', font=('arial', 20))
        l1.pack()

    try:
        str="Shopclues: Rs."
        str=str+shopclues_dict['shopclues']['product_price']
        l1 = Label(root2, text=str,fg="VIOLET", bg = 'white', font = ('arial', 20))
        l1.pack()

    except:
        str = "Shopclues: Sorry! Item not available"
        l1 = Label(root2, text=str, fg="VIOLET", bg='white', font=('arial', 20))
        l1.pack()



def products():
    root1 = Tk()
    root1.geometry("1000x1000")


    search_input = entry.get()

    querystring = {"api_key": api_key, "product": search_input}
    headers = {'content-type': 'application/json'}

    response_search = requests.request("GET", url_search, headers=headers, params=querystring)
    # res_sear_json = response_search.text.read()
    res_sear_json_actual = json.loads(response_search.text)




    for i in range(len(res_sear_json_actual['data'])):


       b=Button(root1,text= (res_sear_json_actual['data'][i]['product_title']),command=partial(detailp,(res_sear_json_actual['data'][i]['product_title'])))
       b.pack()

    root1.mainloop()



root.geometry("900x600")
canvas = Canvas(root, width = 900, height = 300)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("logoprix.png"))
canvas.create_image(20, 20, anchor=NW, image=img)
label2=Label(root, text='Enter item name/product')
label2.pack()
entry=Entry(root)
entry.pack()
button=Button(root,text="search",command=products)
button.pack()
buttone=Button(root,text="Exit",command=dquit,anchor=W)
buttone.pack()
status=Label(root,text="Running....",anchor=W,bg="red")
status.pack(side=BOTTOM,fill=X)
root.mainloop()