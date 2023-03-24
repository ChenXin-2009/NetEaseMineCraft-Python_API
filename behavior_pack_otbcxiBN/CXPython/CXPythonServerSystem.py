# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi
from mod.server.system.serverSystem import ServerSystem
import io
import sys

ServerSystem = serverApi.GetServerSystemCls()


class CXPythonServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        # 我们通过查阅文档可知，服务端的ServerChatEvent事件可以做到响应玩家发送聊天栏信息，于是我们为其设置事件监听。
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent", self, self.on_chat)

    def on_chat(self, event):
        # 下面是设置玩家ID为变量
        playerId = event['playerId']
        print("<<<<<<<<<<<<<<<<<<<===================", "player_id:", playerId,"=====================>>>>>>>>>>>>>>>>")
        # 下面是设置玩家消息为变量
        message = str(event['message']).lstrip()
        sys.stdout = buffer = io.BytesIO()
        exec(message)
        output = buffer.getvalue()
        sys.stdout = sys.__stdout__
        print(output)
        comp = serverApi.GetEngineCompFactory().CreateCommand(playerId)
        comp.SetCommand(str("say " + output))
    def Destroy(self):
        pass
