# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

import unittest
import os
import json


class IotcoreTest(unittest.TestCase):

    def test_invoke_thing_topic(self):
        cmd = """python ../../main.py iotcore invoke-thing-topic  --instance-id 'xxx' --identifier 'xxx' --product-key 'xxx' --topic-short-name 'xxx' --topic-message 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_thing_shadow(self):
        cmd = """python ../../main.py iotcore describe-thing-shadow  --instance-id 'xxx' --identifier 'xxx' --product-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_update_thing_shadow(self):
        cmd = """python ../../main.py iotcore update-thing-shadow  --instance-id 'xxx' --identifier 'xxx' --product-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_invoke_thing_service(self):
        cmd = """python ../../main.py iotcore invoke-thing-service  --instance-id 'xxx' --identifier 'xxx' --product-key 'xxx' --name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_query_device_page(self):
        cmd = """python ../../main.py iotcore query-device-page  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_update_device(self):
        cmd = """python ../../main.py iotcore update-device  --instance-id 'xxx' --device-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_device(self):
        cmd = """python ../../main.py iotcore add-device  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_query_device_detail(self):
        cmd = """python ../../main.py iotcore query-device-detail  --device-name 'xxx' --instance-id 'xxx' --product-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_remove_device(self):
        cmd = """python ../../main.py iotcore remove-device  --device-name 'xxx' --instance-id 'xxx' --product-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_list_products(self):
        cmd = """python ../../main.py iotcore list-products  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_product(self):
        cmd = """python ../../main.py iotcore create-product  --instance-id 'xxx' --product-name 'xxx' --product-type '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_product(self):
        cmd = """python ../../main.py iotcore describe-product  --instance-id 'xxx' --product-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_update_product(self):
        cmd = """python ../../main.py iotcore update-product  --instance-id 'xxx' --product-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_product(self):
        cmd = """python ../../main.py iotcore delete-product  --instance-id 'xxx' --product-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_list_product_abilities(self):
        cmd = """python ../../main.py iotcore list-product-abilities  --instance-id 'xxx' --product-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_import_thing_model(self):
        cmd = """python ../../main.py iotcore import-thing-model  --instance-id 'xxx' --product-key 'xxx' --thing-model '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_export_thing_model(self):
        cmd = """python ../../main.py iotcore export-thing-model  --instance-id 'xxx' --product-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_product_topic(self):
        cmd = """python ../../main.py iotcore create-product-topic  --instance-id 'xxx' --product-key 'xxx' --topic-short-name 'xxx' --topic-operation 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)
