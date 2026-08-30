#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import os
from datetime import datetime

# ----- 你的接口盒子凭证 -----
API_ID = '10020568'
API_KEY = '57dae31c8975b688efd9f2729c3f7cdb'
API_URL = 'http://81.68.85.14/api/zici/today.php'

# 获取今天的月日
now = datetime.now()
month = now.strftime('%m')
day = now.strftime('%d')

def fetch_event():
    params = {
        'id': API_ID,
        'key': API_KEY,
        'm': month,
        'd': day
    }
    try:
        resp = requests.get(API_URL, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if data.get('code') == 200:
            return {
                'year': data.get('y', ''),
                'text': data.get('title', ''),
                'url': data.get('url', '')
            }
        else:
            print(f"API 返回错误: {data.get('msg', '未知错误')}")
            return None
    except Exception as e:
        print(f"请求失败: {e}")
        return None

def main():
    event = fetch_event()
    if event:
        result = {
            'update_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'events': [event]
        }
    else:
        # 如果本次获取失败，保留旧数据（如果存在），仅更新时间戳
        if os.path.exists('history.json'):
            with open('history.json', 'r', encoding='utf-8') as f:
                result = json.load(f)
            result['update_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        else:
            result = {
                'update_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'events': []
            }
    with open('history.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print('history.json 已更新')

if __name__ == '__main__':
    main()
