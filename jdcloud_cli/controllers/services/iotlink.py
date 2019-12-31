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

from argparse import RawTextHelpFormatter
from jdcloud_cli.cement.ext.ext_argparse import expose
from jdcloud_cli.controllers.base_controller import BaseController
from jdcloud_cli.client_factory import ClientFactory
from jdcloud_cli.parameter_builder import collect_user_args, collect_user_headers
from jdcloud_cli.printer import Printer
from jdcloud_cli.skeleton import Skeleton


class IotlinkController(BaseController):
    class Meta:
        label = 'iotlink'
        help = '京东云iotlink接口'
        description = '''
        iotlink cli 子命令，iotlink相关接口。
        OpenAPI文档地址为：https://docs.jdcloud.com/cn/xxx/api/overview
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--iccid'], dict(help="""(string) 物联网卡iccid """, dest='iccid',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 根据物联网卡iccid查询该卡的gprs状态信息 ''',
        description='''
            根据物联网卡iccid查询该卡的gprs状态信息。

            示例: jdc iotlink gprs-status  --iccid xxx
        ''',
    )
    def gprs_status(self):
        client_factory = ClientFactory('iotlink')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iotlink.apis.GprsStatusRequest import GprsStatusRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GprsStatusRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--iccid'], dict(help="""(string) 物联网卡iccid """, dest='iccid',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 根据物联网卡iccid查询该卡的开关机状态信息 ''',
        description='''
            根据物联网卡iccid查询该卡的开关机状态信息。

            示例: jdc iotlink on-off-status  --iccid xxx
        ''',
    )
    def on_off_status(self):
        client_factory = ClientFactory('iotlink')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iotlink.apis.OnOffStatusRequest import OnOffStatusRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = OnOffStatusRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--iccid'], dict(help="""(string) 物联网卡iccid """, dest='iccid',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 根据物联网卡iccid查询该卡的生命周期信息 ''',
        description='''
            根据物联网卡iccid查询该卡的生命周期信息。

            示例: jdc iotlink life-status  --iccid xxx
        ''',
    )
    def life_status(self):
        client_factory = ClientFactory('iotlink')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iotlink.apis.LifeStatusRequest import LifeStatusRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = LifeStatusRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--iccid'], dict(help="""(string) 物联网卡iccid """, dest='iccid',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 根据物联网卡iccid查询该卡的当月套餐内的GPRS实时使用量 ''',
        description='''
            根据物联网卡iccid查询该卡的当月套餐内的GPRS实时使用量。

            示例: jdc iotlink gprs-realtime-info  --iccid xxx
        ''',
    )
    def gprs_realtime_info(self):
        client_factory = ClientFactory('iotlink')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iotlink.apis.GprsRealtimeInfoRequest import GprsRealtimeInfoRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GprsRealtimeInfoRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--iccids'], dict(help="""(array: string) 物联网卡号码列表(单次提交最多不超过200个号码) """, dest='iccids',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 物联网卡开机操作 ''',
        description='''
            物联网卡开机操作。

            示例: jdc iotlink open-iot-card 
        ''',
    )
    def open_iot_card(self):
        client_factory = ClientFactory('iotlink')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iotlink.apis.OpenIotCardRequest import OpenIotCardRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = OpenIotCardRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--iccids'], dict(help="""(array: string) 物联网卡号码列表(单次提交最多不超过200个号码) """, dest='iccids',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 物联网卡停机操作 ''',
        description='''
            物联网卡停机操作。

            示例: jdc iotlink close-iot-card 
        ''',
    )
    def close_iot_card(self):
        client_factory = ClientFactory('iotlink')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iotlink.apis.CloseIotCardRequest import CloseIotCardRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CloseIotCardRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--iccids'], dict(help="""(array: string) 物联网卡号码列表(单次提交最多不超过200个号码) """, dest='iccids',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 物联网卡开启流量操作 ''',
        description='''
            物联网卡开启流量操作。

            示例: jdc iotlink open-iot-flow 
        ''',
    )
    def open_iot_flow(self):
        client_factory = ClientFactory('iotlink')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iotlink.apis.OpenIotFlowRequest import OpenIotFlowRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = OpenIotFlowRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--iccids'], dict(help="""(array: string) 物联网卡号码列表(单次提交最多不超过200个号码) """, dest='iccids',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 物联网卡停流量操作 ''',
        description='''
            物联网卡停流量操作。

            示例: jdc iotlink close-iot-flow 
        ''',
    )
    def close_iot_flow(self):
        client_factory = ClientFactory('iotlink')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iotlink.apis.CloseIotFlowRequest import CloseIotFlowRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CloseIotFlowRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['gprs-status','on-off-status','life-status','gprs-realtime-info','open-iot-card','close-iot-card','open-iot-flow','close-iot-flow',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('iotlink', self.app.pargs.api)
        skeleton.show()