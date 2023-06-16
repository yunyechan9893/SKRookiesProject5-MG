from flask import render_template, request, redirect, url_for
from controller import bp_test as test
import json
import requests
import logging
import environment as env
import time
import datetime


# 마스터페이지 -> 여기 의미 없는 페이지라 나중에 메인페이지로 변경하면 될듯
@test.route('/sim', methods=['GET','post'])
def sim():
  return render_template('test.html')


    
