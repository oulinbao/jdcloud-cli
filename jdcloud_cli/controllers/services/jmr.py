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
from cement.ext.ext_argparse import expose
from jdcloud_cli.controllers.base_controller import BaseController
from jdcloud_cli.client_factory import ClientFactory
from jdcloud_cli.parameter_builder import collect_user_args, collect_user_headers
from jdcloud_cli.printer import Printer
from jdcloud_cli.skeleton import Skeleton


class JmrController(BaseController):
    class Meta:
        label = 'jmr'
        help = '使用该子命令操作jmr相关资源'
        description = '''
        jmr cli 子命令，可以使用该子命令操作jmr相关资源。
        OpenAPI文档地址为：https://www.jdcloud.com/help/detail/413/isCatalog/0
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--cluster-model'], dict(help="""(clusterModel) NA """, dest='clusterModel', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建新集群 ''',
        description='''
            创建新集群。

            示例: jdc jmr create-cluster-in-new-network  --cluster-model {"":""}
        ''',
    )
    def create_cluster_in_new_network(self):
        client_factory = ClientFactory('jmr')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jmr.apis.CreateClusterInNewNetworkRequest import CreateClusterInNewNetworkRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CreateClusterInNewNetworkRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--id'], dict(help="""(string) 集群ID；由八位字符组成 """, dest='id', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询集群详情 ''',
        description='''
            查询集群详情。

            示例: jdc jmr show-cluster-details  --id xxx
        ''',
    )
    def show_cluster_details(self):
        client_factory = ClientFactory('jmr')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jmr.apis.ShowClusterDetailsRequest import ShowClusterDetailsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = ShowClusterDetailsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--id'], dict(help="""(string) 集群ID；由八位字符组成 """, dest='id', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 释放集群 ''',
        description='''
            释放集群。

            示例: jdc jmr release-cluster  --id xxx
        ''',
    )
    def release_cluster(self):
        client_factory = ClientFactory('jmr')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jmr.apis.ReleaseClusterRequest import ReleaseClusterRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = ReleaseClusterRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['create-cluster-in-new-network','show-cluster-details','release-cluster',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('jmr', self.app.pargs.api)
        skeleton.show()
