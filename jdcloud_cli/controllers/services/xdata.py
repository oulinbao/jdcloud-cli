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
from jdcloud_cli.parameter_builder import collect_user_args, collect_user_headers
from jdcloud_cli.printer import Printer
from jdcloud_cli.skeleton import Skeleton


class XdataController(BaseController):
    class Meta:
        label = 'xdata'
        help = '使用该子命令操作xdata相关资源'
        description = '''
        xdata cli 子命令，可以使用该子命令操作xdata相关资源。
        OpenAPI文档地址为：https://www.jdcloud.com/help/detail/389/isCatalog/0
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--instance-name'], dict(help="""(string) 实例名称 """, dest='instanceName', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询数据库列表 ''',
        description='''
            查询数据库列表。

            示例: jdc xdata list-database-info  --instance-name xxx
        ''',
    )
    def list_database_info(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.ListDatabaseInfoRequest import ListDatabaseInfoRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = ListDatabaseInfoRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--database-name'], dict(help="""(string) 数据库名 """, dest='databaseName', required=True)),
            (['--instance-name'], dict(help="""(string) 实例名称 """, dest='instanceName', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询数据库详情 ''',
        description='''
            查询数据库详情。

            示例: jdc xdata get-database-info  --database-name xxx --instance-name xxx
        ''',
    )
    def get_database_info(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.GetDatabaseInfoRequest import GetDatabaseInfoRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetDatabaseInfoRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--database-name'], dict(help="""(string) 数据库名 """, dest='databaseName', required=True)),
            (['--instance-name'], dict(help="""(string) 实例名称 """, dest='instanceName', required=True)),
            (['--description'], dict(help="""(string) 描述信息 """, dest='description', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建数据库 ''',
        description='''
            创建数据库。

            示例: jdc xdata create-database  --database-name xxx --instance-name xxx
        ''',
    )
    def create_database(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.CreateDatabaseRequest import CreateDatabaseRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CreateDatabaseRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--database-name'], dict(help="""(string) 数据库名 """, dest='databaseName', required=True)),
            (['--instance-name'], dict(help="""(string) 实例名称 """, dest='instanceName', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除数据库 ''',
        description='''
            删除数据库。

            示例: jdc xdata delete-database  --database-name xxx --instance-name xxx
        ''',
    )
    def delete_database(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.DeleteDatabaseRequest import DeleteDatabaseRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DeleteDatabaseRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询实例列表 ''',
        description='''
            查询实例列表。

            示例: jdc xdata list-instance-info 
        ''',
    )
    def list_instance_info(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.ListInstanceInfoRequest import ListInstanceInfoRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = ListInstanceInfoRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--database-name'], dict(help="""(string) 数据库名称 """, dest='databaseName', required=False)),
            (['--sql'], dict(help="""(string) sql脚本 """, dest='sql', required=True)),
            (['--user-name'], dict(help="""(string) 用户名称 """, dest='userName', required=True)),
            (['--queue-name'], dict(help="""(string) 队列名称 """, dest='queueName', required=False)),
            (['--source'], dict(help="""(string) 资源名称 """, dest='source', required=False)),
            (['--call-back-url'], dict(help="""(string) 回调地址名称 """, dest='callBackURL', required=False)),
            (['--instance-name'], dict(help="""(string) 实例名称 """, dest='instanceName', required=True)),
            (['--instance-owner-name'], dict(help="""(string) 实例拥有者名称 """, dest='instanceOwnerName', required=False)),
            (['--is-explain'], dict(help="""(string) 是否需要解释 """, dest='isExplain', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 执行Spark SQL ''',
        description='''
            执行Spark SQL。

            示例: jdc xdata execute-ras-query  --sql xxx --user-name xxx --instance-name xxx
        ''',
    )
    def execute_ras_query(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.ExecuteRasQueryRequest import ExecuteRasQueryRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = ExecuteRasQueryRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--script'], dict(help="""(string) PySpark脚本 """, dest='script', required=True)),
            (['--user-name'], dict(help="""(string) 用户名称 """, dest='userName', required=True)),
            (['--instance-name'], dict(help="""(string) 实例名称 """, dest='instanceName', required=True)),
            (['--instance-owner-name'], dict(help="""(string) 实例拥有者名称 """, dest='instanceOwnerName', required=False)),
            (['--script-type'], dict(help="""(string) 脚本类型名称 """, dest='scriptType', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 执行PySpark脚本 ''',
        description='''
            执行PySpark脚本。

            示例: jdc xdata execute-py-spark-query  --script xxx --user-name xxx --instance-name xxx
        ''',
    )
    def execute_py_spark_query(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.ExecutePySparkQueryRequest import ExecutePySparkQueryRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = ExecutePySparkQueryRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--user-name'], dict(help="""(string) 用户名称 """, dest='userName', required=True)),
            (['--query-id'], dict(help="""(string) 查询id名称 """, dest='queryId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获取查询状态 ''',
        description='''
            获取查询状态。

            示例: jdc xdata get-ras-query-state  --user-name xxx --query-id xxx
        ''',
    )
    def get_ras_query_state(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.GetRasQueryStateRequest import GetRasQueryStateRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetRasQueryStateRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--user-name'], dict(help="""(string) 用户名称 """, dest='userName', required=True)),
            (['--query-id'], dict(help="""(string) 查询id """, dest='queryId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获取PySpark脚本的执行状态 ''',
        description='''
            获取PySpark脚本的执行状态。

            示例: jdc xdata get-py-spark-execute-state  --user-name xxx --query-id xxx
        ''',
    )
    def get_py_spark_execute_state(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.GetPySparkExecuteStateRequest import GetPySparkExecuteStateRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetPySparkExecuteStateRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--user-name'], dict(help="""(string) 用户名称 """, dest='userName', required=True)),
            (['--query-id'], dict(help="""(string) 查询id """, dest='queryId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获取查询日志 ''',
        description='''
            获取查询日志。

            示例: jdc xdata get-ras-query-log  --user-name xxx --query-id xxx
        ''',
    )
    def get_ras_query_log(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.GetRasQueryLogRequest import GetRasQueryLogRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetRasQueryLogRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--user-name'], dict(help="""(string) 用户名称 """, dest='userName', required=True)),
            (['--query-id'], dict(help="""(string) 查询id """, dest='queryId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获取查询的结果 ''',
        description='''
            获取查询的结果。

            示例: jdc xdata get-ras-query-result  --user-name xxx --query-id xxx
        ''',
    )
    def get_ras_query_result(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.GetRasQueryResultRequest import GetRasQueryResultRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetRasQueryResultRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--user-name'], dict(help="""(string) 用户名称 """, dest='userName', required=True)),
            (['--query-id'], dict(help="""(string) 查询id """, dest='queryId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获取PySpark执行的结果 ''',
        description='''
            获取PySpark执行的结果。

            示例: jdc xdata get-py-spark-execute-result  --user-name xxx --query-id xxx
        ''',
    )
    def get_py_spark_execute_result(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.GetPySparkExecuteResultRequest import GetPySparkExecuteResultRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetPySparkExecuteResultRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--user-name'], dict(help="""(string) 用户名称 """, dest='userName', required=True)),
            (['--query-id'], dict(help="""(string) 查询id """, dest='queryId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 终止查询 ''',
        description='''
            终止查询。

            示例: jdc xdata cancel-ras-query  --user-name xxx --query-id xxx
        ''',
    )
    def cancel_ras_query(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.CancelRasQueryRequest import CancelRasQueryRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CancelRasQueryRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--user-name'], dict(help="""(string) 用户名称 """, dest='userName', required=True)),
            (['--query-id'], dict(help="""(string) 查询id """, dest='queryId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 终止PySpark任务 ''',
        description='''
            终止PySpark任务。

            示例: jdc xdata cancel-py-spark-job  --user-name xxx --query-id xxx
        ''',
    )
    def cancel_py_spark_job(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.CancelPySparkJobRequest import CancelPySparkJobRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CancelPySparkJobRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--instance-name'], dict(help="""(string) 实例名称 """, dest='instanceName', required=True)),
            (['--database-name'], dict(help="""(string) 数据库名称 """, dest='databaseName', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询指定数据库下所有数据表 ''',
        description='''
            查询指定数据库下所有数据表。

            示例: jdc xdata list-table-info  --instance-name xxx --database-name xxx
        ''',
    )
    def list_table_info(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.ListTableInfoRequest import ListTableInfoRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = ListTableInfoRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--instance-name'], dict(help="""(string) 实例名称 """, dest='instanceName', required=True)),
            (['--db-model-dbtable'], dict(help="""(dwTableDesc) 数据表描述 """, dest='dbModelDBTable', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建数据表 ''',
        description='''
            创建数据表。

            示例: jdc xdata create-table  --instance-name xxx --db-model-dbtable {"":""}
        ''',
    )
    def create_table(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.CreateTableRequest import CreateTableRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CreateTableRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--table-name'], dict(help="""(string) 数据表名 """, dest='tableName', required=True)),
            (['--instance-name'], dict(help="""(string) 实例名称 """, dest='instanceName', required=True)),
            (['--database-name'], dict(help="""(string) 数据库名称 """, dest='databaseName', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询数据表信息 ''',
        description='''
            查询数据表信息。

            示例: jdc xdata get-table-info  --table-name xxx --instance-name xxx --database-name xxx
        ''',
    )
    def get_table_info(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.GetTableInfoRequest import GetTableInfoRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetTableInfoRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--table-name'], dict(help="""(string) 数据表名 """, dest='tableName', required=True)),
            (['--instance-name'], dict(help="""(string) 实例名称 """, dest='instanceName', required=True)),
            (['--database-name'], dict(help="""(string) 数据库名称 """, dest='databaseName', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除数据表 ''',
        description='''
            删除数据表。

            示例: jdc xdata delete-table  --table-name xxx --instance-name xxx --database-name xxx
        ''',
    )
    def delete_table(self):
        client_factory = ClientFactory('xdata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.xdata.apis.DeleteTableRequest import DeleteTableRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DeleteTableRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['list-database-info','get-database-info','create-database','delete-database','list-instance-info','execute-ras-query','execute-py-spark-query','get-ras-query-state','get-py-spark-execute-state','get-ras-query-log','get-ras-query-result','get-py-spark-execute-result','cancel-ras-query','cancel-py-spark-job','list-table-info','create-table','get-table-info','delete-table',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('xdata', self.app.pargs.api)
        skeleton.show()
