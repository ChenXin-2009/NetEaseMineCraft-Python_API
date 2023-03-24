# -*- coding: utf-8 -*-

from common.mod import Mod
import mod.server.extraServerApi as serverApi

@Mod.Binding(name="CXPython", version="0.0.1")
class CXPython(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def C_Xin_kscsModServerInit(self):
        serverApi.RegisterSystem("CXPython", "CXPython_System", "CXPython.CXPythonServerSystem.CXPythonServerSystem")
        print("======================================================================================\n")
        print("==<<<<====<<<<>>>>>>>>=====CXPythonServerInit调用成功！！！===<<<<=====<<<<>>>>>>>>")
        print("======================================================================================\n")

    @Mod.DestroyServer()
    def CXPythonServerDestroy(self):
        pass

    @Mod.InitClient()
    def CXPythonClientInit(self):
        pass

    @Mod.DestroyClient()
    def CXPythonClientDestroy(self):
        pass
