# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
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
from jdcloud_cli.parameter_builder import collect_user_args
from jdcloud_cli.printer import Printer
from jdcloud_cli.skeleton import Skeleton


class IpantiController(BaseController):
    class Meta:
        label = 'ipanti'
        help = '使用该子命令操作ipanti相关资源'
        description = '''
        ipanti cli 子命令，可以使用该子命令操作ipanti相关资源。
        OpenAPI文档地址为：https://www.jdcloud.com/help/detail/381/isCatalog/0
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--page-number'], dict(help="""(int) 页码；默认为1 """, dest='pageNumber', required=False)),
            (['--page-size'], dict(help="""(int) 分页大小；默认为20；取值范围[10, 100] """, dest='pageSize', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询某个实例下的非网站转发配置 ''',
        description='''
            查询某个实例下的非网站转发配置。

            示例: jdc ipanti describe-forward-rules  --instance-id xxx
        ''',
    )
    def describe_forward_rules(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.DescribeForwardRulesRequest import DescribeForwardRulesRequest
            params_dict = collect_user_args(self.app)
            req = DescribeForwardRulesRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--forward-rule-spec'], dict(help="""(forwardRuleSpec) 非网站类规则参数 """, dest='forwardRuleSpec', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 添加非网站类规则 ''',
        description='''
            添加非网站类规则。

            示例: jdc ipanti create-forward-rule  --instance-id xxx --forward-rule-spec {"":""}
        ''',
    )
    def create_forward_rule(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.CreateForwardRuleRequest import CreateForwardRuleRequest
            params_dict = collect_user_args(self.app)
            req = CreateForwardRuleRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--forward-rule-id'], dict(help="""(string) 转发规则id """, dest='forwardRuleId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询某条非网站类规则 ''',
        description='''
            查询某条非网站类规则。

            示例: jdc ipanti describe-forward-rule  --instance-id xxx --forward-rule-id xxx
        ''',
    )
    def describe_forward_rule(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.DescribeForwardRuleRequest import DescribeForwardRuleRequest
            params_dict = collect_user_args(self.app)
            req = DescribeForwardRuleRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--forward-rule-id'], dict(help="""(string) 转发规则id """, dest='forwardRuleId', required=True)),
            (['--forward-rule-spec'], dict(help="""(forwardRuleSpec) 非网站类规则参数 """, dest='forwardRuleSpec', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 更新某条非网站类规则 ''',
        description='''
            更新某条非网站类规则。

            示例: jdc ipanti modify-forward-rule  --instance-id xxx --forward-rule-id xxx --forward-rule-spec {"":""}
        ''',
    )
    def modify_forward_rule(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.ModifyForwardRuleRequest import ModifyForwardRuleRequest
            params_dict = collect_user_args(self.app)
            req = ModifyForwardRuleRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--forward-rule-id'], dict(help="""(string) 转发规则id """, dest='forwardRuleId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除某条非网站规则 ''',
        description='''
            删除某条非网站规则。

            示例: jdc ipanti delete-forward-rule  --instance-id xxx --forward-rule-id xxx
        ''',
    )
    def delete_forward_rule(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.DeleteForwardRuleRequest import DeleteForwardRuleRequest
            params_dict = collect_user_args(self.app)
            req = DeleteForwardRuleRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--page-number'], dict(help="""(int) 页码；默认为1 """, dest='pageNumber', required=False)),
            (['--page-size'], dict(help="""(int) 分页大小；默认为20；取值范围[10, 100] """, dest='pageSize', required=False)),
            (['--name'], dict(help="""(string) 实例名称，可模糊匹配 """, dest='name', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询实例列表 ''',
        description='''
            查询实例列表。

            示例: jdc ipanti describe-instances 
        ''',
    )
    def describe_instances(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.DescribeInstancesRequest import DescribeInstancesRequest
            params_dict = collect_user_args(self.app)
            req = DescribeInstancesRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-spec'], dict(help="""(instanceSpec) 实例规格参数 """, dest='instanceSpec', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建实例 ''',
        description='''
            创建实例。

            示例: jdc ipanti create-instance  --instance-spec {"":""}
        ''',
    )
    def create_instance(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.CreateInstanceRequest import CreateInstanceRequest
            params_dict = collect_user_args(self.app)
            req = CreateInstanceRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询实例 ''',
        description='''
            查询实例。

            示例: jdc ipanti describe-instance  --instance-id xxx
        ''',
    )
    def describe_instance(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.DescribeInstanceRequest import DescribeInstanceRequest
            params_dict = collect_user_args(self.app)
            req = DescribeInstanceRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--c-cspec'], dict(help="""(cCSpec) cc参数 """, dest='cCSpec', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 设置实例CC防护 ''',
        description='''
            设置实例CC防护。

            示例: jdc ipanti modify-instance-cc  --instance-id xxx --c-cspec {"":""}
        ''',
    )
    def modify_instance_cc(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.ModifyInstanceCCRequest import ModifyInstanceCCRequest
            params_dict = collect_user_args(self.app)
            req = ModifyInstanceCCRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 开启实例CC防护 ''',
        description='''
            开启实例CC防护。

            示例: jdc ipanti enable-instance-cc  --instance-id xxx
        ''',
    )
    def enable_instance_cc(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.EnableInstanceCCRequest import EnableInstanceCCRequest
            params_dict = collect_user_args(self.app)
            req = EnableInstanceCCRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 关闭实例CC防护 ''',
        description='''
            关闭实例CC防护。

            示例: jdc ipanti disable-instance-cc  --instance-id xxx
        ''',
    )
    def disable_instance_cc(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.DisableInstanceCCRequest import DisableInstanceCCRequest
            params_dict = collect_user_args(self.app)
            req = DisableInstanceCCRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--url-white-list'], dict(help="""(array: string) 网站类规则参数 """, dest='urlWhiteList', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 设置实例url白名单 ''',
        description='''
            设置实例url白名单。

            示例: jdc ipanti modify-instance-url-white-list  --instance-id xxx
        ''',
    )
    def modify_instance_url_white_list(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.ModifyInstanceUrlWhiteListRequest import ModifyInstanceUrlWhiteListRequest
            params_dict = collect_user_args(self.app)
            req = ModifyInstanceUrlWhiteListRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 启用实例url白名单 ''',
        description='''
            启用实例url白名单。

            示例: jdc ipanti enable-instance-url-white-list  --instance-id xxx
        ''',
    )
    def enable_instance_url_white_list(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.EnableInstanceUrlWhiteListRequest import EnableInstanceUrlWhiteListRequest
            params_dict = collect_user_args(self.app)
            req = EnableInstanceUrlWhiteListRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 禁用实例url白名单 ''',
        description='''
            禁用实例url白名单。

            示例: jdc ipanti disable-instance-url-white-list  --instance-id xxx
        ''',
    )
    def disable_instance_url_white_list(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.DisableInstanceUrlWhiteListRequest import DisableInstanceUrlWhiteListRequest
            params_dict = collect_user_args(self.app)
            req = DisableInstanceUrlWhiteListRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--name'], dict(help="""(string) 新的实例名称 """, dest='name', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 修改实例名称 ''',
        description='''
            修改实例名称。

            示例: jdc ipanti modify-instance-name  --instance-id xxx --name xxx
        ''',
    )
    def modify_instance_name(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.ModifyInstanceNameRequest import ModifyInstanceNameRequest
            params_dict = collect_user_args(self.app)
            req = ModifyInstanceNameRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--ip-black-list'], dict(help="""(array: string) ip黑名单列表 """, dest='ipBlackList', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 设置实例ip黑名单 ''',
        description='''
            设置实例ip黑名单。

            示例: jdc ipanti modify-instance-ip-black-list  --instance-id xxx
        ''',
    )
    def modify_instance_ip_black_list(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.ModifyInstanceIpBlackListRequest import ModifyInstanceIpBlackListRequest
            params_dict = collect_user_args(self.app)
            req = ModifyInstanceIpBlackListRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 启用实例ip黑名单 ''',
        description='''
            启用实例ip黑名单。

            示例: jdc ipanti enable-instance-ip-black-list  --instance-id xxx
        ''',
    )
    def enable_instance_ip_black_list(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.EnableInstanceIpBlackListRequest import EnableInstanceIpBlackListRequest
            params_dict = collect_user_args(self.app)
            req = EnableInstanceIpBlackListRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 禁用实例ip黑名单 ''',
        description='''
            禁用实例ip黑名单。

            示例: jdc ipanti disable-instance-ip-black-list  --instance-id xxx
        ''',
    )
    def disable_instance_ip_black_list(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.DisableInstanceIpBlackListRequest import DisableInstanceIpBlackListRequest
            params_dict = collect_user_args(self.app)
            req = DisableInstanceIpBlackListRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--ip-white-list'], dict(help="""(array: string) ip白名单列表 """, dest='ipWhiteList', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 设置实例ip白名单 ''',
        description='''
            设置实例ip白名单。

            示例: jdc ipanti modify-instance-ip-white-list  --instance-id xxx
        ''',
    )
    def modify_instance_ip_white_list(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.ModifyInstanceIpWhiteListRequest import ModifyInstanceIpWhiteListRequest
            params_dict = collect_user_args(self.app)
            req = ModifyInstanceIpWhiteListRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 启用实例ip白名单 ''',
        description='''
            启用实例ip白名单。

            示例: jdc ipanti enable-instance-ip-white-list  --instance-id xxx
        ''',
    )
    def enable_instance_ip_white_list(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.EnableInstanceIpWhiteListRequest import EnableInstanceIpWhiteListRequest
            params_dict = collect_user_args(self.app)
            req = EnableInstanceIpWhiteListRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 禁用实例ip白名单 ''',
        description='''
            禁用实例ip白名单。

            示例: jdc ipanti disable-instance-ip-white-list  --instance-id xxx
        ''',
    )
    def disable_instance_ip_white_list(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.DisableInstanceIpWhiteListRequest import DisableInstanceIpWhiteListRequest
            params_dict = collect_user_args(self.app)
            req = DisableInstanceIpWhiteListRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--page-number'], dict(help="""(int) 页码；默认为1 """, dest='pageNumber', required=False)),
            (['--page-size'], dict(help="""(int) 分页大小；默认为20；取值范围[10, 100] """, dest='pageSize', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询某个实例下的网站类规则 ''',
        description='''
            查询某个实例下的网站类规则。

            示例: jdc ipanti describe-web-rules  --instance-id xxx
        ''',
    )
    def describe_web_rules(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.DescribeWebRulesRequest import DescribeWebRulesRequest
            params_dict = collect_user_args(self.app)
            req = DescribeWebRulesRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--web-rule-spec'], dict(help="""(webRuleSpec) 网站类规则参数 """, dest='webRuleSpec', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 添加网站类规则 ''',
        description='''
            添加网站类规则。

            示例: jdc ipanti create-web-rule  --instance-id xxx --web-rule-spec {"":""}
        ''',
    )
    def create_web_rule(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.CreateWebRuleRequest import CreateWebRuleRequest
            params_dict = collect_user_args(self.app)
            req = CreateWebRuleRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--web-rule-id'], dict(help="""(string) 网站规则id """, dest='webRuleId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询某条网站类规则 ''',
        description='''
            查询某条网站类规则。

            示例: jdc ipanti describe-web-rule  --instance-id xxx --web-rule-id xxx
        ''',
    )
    def describe_web_rule(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.DescribeWebRuleRequest import DescribeWebRuleRequest
            params_dict = collect_user_args(self.app)
            req = DescribeWebRuleRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--web-rule-id'], dict(help="""(string) 网站规则id """, dest='webRuleId', required=True)),
            (['--web-rule-spec'], dict(help="""(webRuleSpec) 网站类规则参数 """, dest='webRuleSpec', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 更新某条网站类规则 ''',
        description='''
            更新某条网站类规则。

            示例: jdc ipanti modify-web-rule  --instance-id xxx --web-rule-id xxx --web-rule-spec {"":""}
        ''',
    )
    def modify_web_rule(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.ModifyWebRuleRequest import ModifyWebRuleRequest
            params_dict = collect_user_args(self.app)
            req = ModifyWebRuleRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例id """, dest='instanceId', required=True)),
            (['--web-rule-id'], dict(help="""(string) 网站规则id """, dest='webRuleId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除某条网站规则 ''',
        description='''
            删除某条网站规则。

            示例: jdc ipanti delete-web-rule  --instance-id xxx --web-rule-id xxx
        ''',
    )
    def delete_web_rule(self):
        client_factory = ClientFactory('ipanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ipanti.apis.DeleteWebRuleRequest import DeleteWebRuleRequest
            params_dict = collect_user_args(self.app)
            req = DeleteWebRuleRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['describe-forward-rules','create-forward-rule','describe-forward-rule','modify-forward-rule','delete-forward-rule','describe-instances','create-instance','describe-instance','modify-instance-cc','enable-instance-cc','disable-instance-cc','modify-instance-url-white-list','enable-instance-url-white-list','disable-instance-url-white-list','modify-instance-name','modify-instance-ip-black-list','enable-instance-ip-black-list','disable-instance-ip-black-list','modify-instance-ip-white-list','enable-instance-ip-white-list','disable-instance-ip-white-list','describe-web-rules','create-web-rule','describe-web-rule','modify-web-rule','delete-web-rule',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('ipanti', self.app.pargs.api)
        skeleton.show()