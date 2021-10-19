"""
Запуск сервера осуществляется при помощи вызова main
"""

from flask import render_template, url_for
from app import app
import torch


if __name__ == "__main__":

    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./best.pt').autoshape()
    model.conf = 0.25  # confidence threshold (0-1)
    model.iou = 0.50
    print(dir(model))
    model.eval()
    app.run()
