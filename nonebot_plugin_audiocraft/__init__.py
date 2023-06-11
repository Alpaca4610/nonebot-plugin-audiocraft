import io
from gradio_client import Client
import nonebot

from nonebot.plugin import PluginMetadata
from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Message, MessageSegment


__plugin_meta__ = PluginMetadata(
    name="AI作曲",
    description="Nonebot框架下的AI作曲插件",
    usage=
    '''
    每次重启机器人后，使用 %%后端服务器地址 绑定audiocraft后端服务器。
    绑定后端服务器后，使用 AI作曲+乐曲的英文描述 即可触发AI作曲。
    ''',
    config="",
    extra={},
)

url = ""
direct = on_command("AI作曲", block=False, priority=1)


@direct.handle()
async def _(msg: Message = CommandArg()):
    content = msg.extract_plain_text()
    if content == "" or content is None:
        await direct.finish(MessageSegment.text("内容不能为空！"))
    if url == "" or url is None:
        await direct.finish(MessageSegment.text("未设置服务器！"))

    await direct.send(MessageSegment.text("audiocraft正在努力作曲中......"))

    client = Client(url)
    result = client.predict(
                    "small",	# str  in 'Model' Radio component
                    content,	# str  in 'Input Text' Textbox component
                    "",	# str (filepath or URL to file) in 'Melody Condition (optional)' Audio component
                    6,	# int | float (numeric value between 1 and 30) in 'Duration' Slider component
                    250,	# int | float  in 'Top-k' Number component
                    0,	# int | float  in 'Top-p' Number component
                    1,	# int | float  in 'Temperature' Number component
                    3,	# int | float  in 'Classifier Free Guidance' Number component
                    fn_index=0
    )
    print(result)


    with open(result, "rb") as file:
        file_content = file.read()
        audio = io.BytesIO(file_content) 
        await direct.finish(MessageSegment.record(file=audio))


config_url = on_command("%%", block=False, priority=1)


@config_url.handle()
async def _(msg: Message = CommandArg()):
    global url
    url_ = msg.extract_plain_text()
    if url_ == "" or url_ is None:
        await config_url.finish(MessageSegment.text("内容不能为空！"))
    url = url_
    await config_url.finish(MessageSegment.text(f"成功设置地址为{url_}"))

