#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   sync.py
@Time    :   2023/02/14
@Author  :   Junxiao Guo
@Version :   1.0
@License :   (C)Copyright 2022-2023, Junxiao Guo
@Desc    :   DB Sync for data
'''
import os
import json
import logging
import requests
from pathlib import Path
from dotenv import load_dotenv


logging.basicConfig(encoding='utf-8', level=logging.INFO)

load_dotenv()

API_ENDPOINT = os.environ.get("API_ENDPOINT")
API_TOKEN = os.environ.get("API_TOKEN")

headers = {"Content-Type": "application/json; charset=utf-8",
           "Authorization": f"Token {API_TOKEN}"}

with open(Path.cwd().parent.joinpath('data/experience.json'), 'r', encoding='utf-8') as expfile:
    data = json.load(expfile)
    for exp in data:
        response = requests.post(API_ENDPOINT, headers=headers,
                                 json=exp,
                                 timeout=300)
        if response.status_code != 201:
            logging.error("Failed to post experience.")