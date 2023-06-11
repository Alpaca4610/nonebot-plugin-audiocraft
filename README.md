<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-audiocraft
</div>

# 介绍
- 本插件适配[Facebook开源的AI作曲模型](https://github.com/facebookresearch/audiocraft/)，在nonebot框架下调用已经部署好的模型后端服务器API进行AI作曲
- 本插件需要配合部署好的audiocraft进行使用

# 安装

* 手动安装
  ```
  git clone https://github.com/Alpaca4610/nonebot_plugin_audiocraft.git
  ```

  下载完成后在bot项目的pyproject.toml文件手动添加插件：

  ```
  plugin_dirs = ["xxxxxx","xxxxxx",......,"下载完成的插件路径/nonebot-plugin-audiocraft"]
  ```
* 使用 pip
  ```
  pip install nonebot-plugin-audiocraft
  ```
# 后端服务器部署
参考[官方仓库](https://github.com/facebookresearch/audiocraft#usage)部署好gradio后端，获得后端网址。（coblab上部署的可以开启gradio的外链分享）


# 使用方法

- 由于最近tx风控严重，go-cqhttp面临重启后可能掉账号的风险，所以插件使用给机器人发送消息配置后端服务器配置的方法。
- 每次重启机器人后，使用 %%后端服务器地址 绑定audiocraft后端服务器。
- 绑定后端服务器后，使用 AI作曲+乐曲的英文描述 即可触发AI作曲。
- AI作曲的参数（如模型、时长）等通过代码进行修改，代码中有注释说明。

# 效果

![Alt](demo1.png)
![Alt](demo2.png)
