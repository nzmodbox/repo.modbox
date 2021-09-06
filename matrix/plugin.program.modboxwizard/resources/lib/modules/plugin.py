import xbmc
import xbmcplugin
import sys
from .params import Params
from addonvar import addon
from .utils import play_video
from .menus import main_menu, build_menu, submenu_maintenance, authorize_menu
from .build_install import main
from .maintenance import fresh_start, clear_packages, clear_thumbnails, advanced_settings

handle = int(sys.argv[1])

def router(paramstring):
    p = Params(paramstring)
    xbmc.log(str(p.get_params()),xbmc.LOGDEBUG)
    
    name = p.get_name()
    name2 = p.get_name2()
    version = p.get_version()
    url = p.get_url()
    mode = p.get_mode()
    icon = p.get_icon()
    fanart = p.get_fanart()
    description = p.get_description()
    
    xbmcplugin.setContent(handle, 'files')

    if mode is None:
    	main_menu()
    
    elif mode == 1:
    	build_menu()
    
    elif mode == 2:
    	play_video(name, url, icon, description)
    
    elif mode == 3:
    	main(name, name2, version, url)
    
    elif mode == 4:
    	fresh_start(standalone=True)
    
    elif mode == 5:
    	submenu_maintenance()
    
    elif mode == 6:
    	clear_packages()
    
    elif mode == 7:
    	clear_thumbnails()
    
    elif mode == 8:
    	advanced_settings()
    
    elif mode == 9:
    	addon.openSettings()
    
    elif mode == 10:
    	authorize_menu()
    
    elif mode == 100:
    	from resources.lib.GUIcontrol import notify
    	d=notify.notify()
    	d.doModal()
    	del d
    	
    xbmcplugin.endOfDirectory(handle)