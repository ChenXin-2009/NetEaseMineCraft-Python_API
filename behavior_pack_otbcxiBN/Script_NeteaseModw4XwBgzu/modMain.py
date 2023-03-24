# -*- coding: utf-8 -*-

from common.mod import Mod


@Mod.Binding(name="Script_NeteaseModw4XwBgzu", version="0.0.1")
class Script_NeteaseModw4XwBgzu(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModw4XwBgzuServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModw4XwBgzuServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModw4XwBgzuClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModw4XwBgzuClientDestroy(self):
        pass
