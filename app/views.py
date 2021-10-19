import os
from flask import Blueprint, render_template, redirect, url_for, request, flash, send_file, send_from_directory
from app import app, db
from PIL import Image
import argparse
import io
import torch


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        model = torch.hub.load('ultralytics/yolov5', 'custom', path='./best.pt').autoshape() #Обученная модель
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if not file:
            return

        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        results = model(img, size=640)
        results.render()

        pics = [os.path.join('./app/static/pic/', x) for x in os.listdir('./app/static/pic/') if x[-3:] == "jpg"]
        pics.sort(key=lambda x: int(x.split('image')[1].split('.')[0]))
        path = os.path.abspath("./app/static/pic/image"+str(len(pics))+".jpg")

        for img in results.imgs:
            img_base64 = Image.fromarray(img)

            img_base64.save(path, format="JPEG")

        return redirect("static/pic/image"+str(len(pics))+".jpg")

    return render_template("photo.html")


