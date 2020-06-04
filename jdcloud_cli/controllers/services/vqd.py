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


class VqdController(BaseController):
    class Meta:
        label = 'vqd'
        help = 'Video Quality Detection'
        description = '''
        vqd cli 子命令，视频质量检测相关接口。
        OpenAPI文档地址为：https://docs.jdcloud.com/cn/xxx/api/overview
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--callback-type'], dict(help="""(string) 回调方式，目前只支持 http """, dest='callbackType',  required=True)),
            (['--http-url'], dict(help="""(string) HTTP方式的该字段为必选项 """, dest='httpUrl',  required=False)),
            (['--callback-events'], dict(help="""(array: string) 回调事件列表。; - VqdSuccess 视频质检成功; - VqdFailure 视频质检失败; - VqdStart 视频质检开始;  """, dest='callbackEvents',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 设置回调配置 ''',
        description='''
            设置回调配置。

            示例: jdc vqd set-callback  --callback-type xxx
        ''',
    )
    def set_callback(self):
        client_factory = ClientFactory('vqd')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vqd.apis.SetCallbackRequest import SetCallbackRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = SetCallbackRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询回调配置 ''',
        description='''
            查询回调配置。

            示例: jdc vqd query-callback 
        ''',
    )
    def query_callback(self):
        client_factory = ClientFactory('vqd')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vqd.apis.QueryCallbackRequest import QueryCallbackRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = QueryCallbackRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--media'], dict(help="""(vqdMediaObject) NA """, dest='media',  required=True)),
            (['--template-id'], dict(help="""(string) 检测模板ID """, dest='templateId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 提交视频质检任务 ''',
        description='''
            提交视频质检任务。

            示例: jdc vqd submit-vqd-task  --media '{"":""}' --template-id xxx
        ''',
    )
    def submit_vqd_task(self):
        client_factory = ClientFactory('vqd')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vqd.apis.SubmitVqdTaskRequest import SubmitVqdTaskRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = SubmitVqdTaskRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--media-list'], dict(help="""(array: vqdMediaObject) 媒体列表 """, dest='mediaList',  required=True)),
            (['--template-id'], dict(help="""(string) 检测模板ID """, dest='templateId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 批量提交视频质检任务，一次同时最多提交50个输入媒体 ''',
        description='''
            批量提交视频质检任务，一次同时最多提交50个输入媒体。

            示例: jdc vqd batch-submit-vqd-tasks  --media-list ['{"":""}'] --template-id xxx
        ''',
    )
    def batch_submit_vqd_tasks(self):
        client_factory = ClientFactory('vqd')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vqd.apis.BatchSubmitVqdTasksRequest import BatchSubmitVqdTasksRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = BatchSubmitVqdTasksRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--page-number'], dict(help="""(int) 页码；默认值为 1 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小；默认值为 10；取值范围 [10, 100] """, dest='pageSize', type=int, required=False)),
            (['--filters'], dict(help="""(array: filter) NA """, dest='filters',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询视频质检任务列表; 支持过滤查询：;   - createTime,ge 最早任务创建时间;   - createTime,le 最晚任务创建时间;   - status,in 任务状态;  ''',
        description='''
            查询视频质检任务列表; 支持过滤查询：;   - createTime,ge 最早任务创建时间;   - createTime,le 最晚任务创建时间;   - status,in 任务状态; 。

            示例: jdc vqd list-vqd-tasks 
        ''',
    )
    def list_vqd_tasks(self):
        client_factory = ClientFactory('vqd')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vqd.apis.ListVqdTasksRequest import ListVqdTasksRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = ListVqdTasksRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--task-id'], dict(help="""(string) 任务ID，路径参数 """, dest='taskId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获取视频质检任务详细信息 ''',
        description='''
            获取视频质检任务详细信息。

            示例: jdc vqd get-vqd-task  --task-id xxx
        ''',
    )
    def get_vqd_task(self):
        client_factory = ClientFactory('vqd')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vqd.apis.GetVqdTaskRequest import GetVqdTaskRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetVqdTaskRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--task-id'], dict(help="""(string) 任务ID，路径参数 """, dest='taskId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除视频质检任务。删除任务时，会同时删除任务相关的数据，如任务执行结果等 ''',
        description='''
            删除视频质检任务。删除任务时，会同时删除任务相关的数据，如任务执行结果等。

            示例: jdc vqd delete-vqd-task  --task-id xxx
        ''',
    )
    def delete_vqd_task(self):
        client_factory = ClientFactory('vqd')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vqd.apis.DeleteVqdTaskRequest import DeleteVqdTaskRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DeleteVqdTaskRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--task-id'], dict(help="""(string) 任务ID，路径参数 """, dest='taskId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询视频质检任务结果 ''',
        description='''
            查询视频质检任务结果。

            示例: jdc vqd query-vqd-task-result  --task-id xxx
        ''',
    )
    def query_vqd_task_result(self):
        client_factory = ClientFactory('vqd')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vqd.apis.QueryVqdTaskResultRequest import QueryVqdTaskResultRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = QueryVqdTaskResultRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--task-ids'], dict(help="""(array: string) NA """, dest='taskIds',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 批量删除视频质检任务。删除任务时，会同时删除任务相关的数据，如任务执行结果等。一次最多删除50条 ''',
        description='''
            批量删除视频质检任务。删除任务时，会同时删除任务相关的数据，如任务执行结果等。一次最多删除50条。

            示例: jdc vqd batch-delete-vqd-tasks 
        ''',
    )
    def batch_delete_vqd_tasks(self):
        client_factory = ClientFactory('vqd')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vqd.apis.BatchDeleteVqdTasksRequest import BatchDeleteVqdTasksRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = BatchDeleteVqdTasksRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--page-number'], dict(help="""(int) 页码；默认值为 1 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小；默认值为 10；取值范围 [10, 100] """, dest='pageSize', type=int, required=False)),
            (['--filters'], dict(help="""(array: filter) NA """, dest='filters',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询视频质检模板列表。; 支持过滤查询：;   - templateId,eq 精确匹配模板ID，非必选;  ''',
        description='''
            查询视频质检模板列表。; 支持过滤查询：;   - templateId,eq 精确匹配模板ID，非必选; 。

            示例: jdc vqd list-vqd-templates 
        ''',
    )
    def list_vqd_templates(self):
        client_factory = ClientFactory('vqd')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vqd.apis.ListVqdTemplatesRequest import ListVqdTemplatesRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = ListVqdTemplatesRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--template-name'], dict(help="""(string) 模板名称。长度不超过128个字符。UTF-8编码。;  """, dest='templateName',  required=True)),
            (['--threshold'], dict(help="""(float) 缺陷判定时间阈值，非必须，默认值为 3.0 """, dest='threshold',  required=False)),
            (['--detections'], dict(help="""(array: string) 检测项列表 """, dest='detections',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建视频质检模板 ''',
        description='''
            创建视频质检模板。

            示例: jdc vqd create-vqd-template  --template-name xxx
        ''',
    )
    def create_vqd_template(self):
        client_factory = ClientFactory('vqd')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vqd.apis.CreateVqdTemplateRequest import CreateVqdTemplateRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CreateVqdTemplateRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--template-id'], dict(help="""(string) 模板ID，路径参数 """, dest='templateId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询视频质检模板 ''',
        description='''
            查询视频质检模板。

            示例: jdc vqd get-vqd-template  --template-id xxx
        ''',
    )
    def get_vqd_template(self):
        client_factory = ClientFactory('vqd')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vqd.apis.GetVqdTemplateRequest import GetVqdTemplateRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetVqdTemplateRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--template-id'], dict(help="""(string) 模板ID，路径参数 """, dest='templateId',  required=True)),
            (['--template-name'], dict(help="""(string) 模板名称。长度不超过128个字符。UTF-8编码。;  """, dest='templateName',  required=False)),
            (['--threshold'], dict(help="""(float) 缺陷判定时间阈值 """, dest='threshold',  required=False)),
            (['--detections'], dict(help="""(array: string) 检测项列表 """, dest='detections',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 修改视频质检模板 ''',
        description='''
            修改视频质检模板。

            示例: jdc vqd update-vqd-template  --template-id xxx
        ''',
    )
    def update_vqd_template(self):
        client_factory = ClientFactory('vqd')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vqd.apis.UpdateVqdTemplateRequest import UpdateVqdTemplateRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = UpdateVqdTemplateRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--template-id'], dict(help="""(string) 模板ID，路径参数 """, dest='templateId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除视频质检模板 ''',
        description='''
            删除视频质检模板。

            示例: jdc vqd delete-vqd-template  --template-id xxx
        ''',
    )
    def delete_vqd_template(self):
        client_factory = ClientFactory('vqd')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vqd.apis.DeleteVqdTemplateRequest import DeleteVqdTemplateRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DeleteVqdTemplateRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['set-callback','query-callback','submit-vqd-task','batch-submit-vqd-tasks','list-vqd-tasks','get-vqd-task','delete-vqd-task','query-vqd-task-result','batch-delete-vqd-tasks','list-vqd-templates','create-vqd-template','get-vqd-template','update-vqd-template','delete-vqd-template',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('vqd', self.app.pargs.api)
        skeleton.show()