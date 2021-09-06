import sys
import json
import xbmcplugin
import xbmcvfs
from .utils import add_dir
from .parser import Parser
from .dropbox import DownloadFile
from addonvar import addon_icon, addon_fanart, local_string, buildfile, build_file, authorize

handle = int(sys.argv[1])

def main_menu():
	xbmcplugin.setPluginCategory(handle, 'Main Menu')
	
	add_dir(local_string(30010),'',1,addon_icon,addon_fanart,local_string(30001),isFolder=True)  # Build Menu
	
	add_dir(local_string(30011),'',5,addon_icon,addon_fanart,local_string(30002),isFolder=True)  # Maintenance
	
	add_dir(local_string(30012),'',4,addon_icon,addon_fanart,local_string(30003),isFolder=False)  # Fresh Start
	
	add_dir(local_string(30013),'',100,addon_icon,addon_fanart,local_string(30014),isFolder=False)  # Notification
	
	add_dir(local_string(30015),'',9,addon_icon,addon_fanart,local_string(30016),isFolder=False)  # Settings

def build_menu():
    xbmcplugin.setPluginCategory(handle, local_string(30010))
    if buildfile.startswith('https://www.dropbox.com'):
    	if not xbmcvfs.exists(build_file):
    		DownloadFile(buildfile, build_file)
    	builds = json.load(open(build_file,'r')).get('builds')
    elif not buildfile.endswith('.xml') and not buildfile.endswith('.json'):
    	add_dir(local_string(30017),'','',addon_icon,addon_fanart,local_string(30017),isFolder=False)  # Invalid Build URL
    	return
    else:
    	p = Parser(buildfile)
    	builds = json.loads(p.get_list())['builds']
    
    for build in builds:
    	name = (build.get('name', local_string(30018)))  # Unknown Name
    	version = (build.get('version', '0'))
    	url = (build.get('url', ''))
    	icon = (build.get('icon', addon_icon))
    	fanart = (build.get('fanart', addon_fanart))
    	description = (build.get('description', local_string(30019)))  # No Description Available.
    	preview = (build.get('preview',None))
    	
    	if url.endswith('.xml') or url.endswith('.json'):
    		add_dir(name,url,1,icon,fanart,description,name2=name,version=version,isFolder=True)
    	add_dir(name + ' ' + local_string(30020) + ' ' + version,url,3,icon,fanart,description,name2=name,version=version,isFolder=False)  # Version
    	if preview is not None:
    		add_dir(local_string(30021) + ' ' + name + ' ' + local_string(30020) + ' ' + version,preview,2,icon,fanart,description,name2=name,version=version,isFolder=False)  # Video Preview

def submenu_maintenance():
	xbmcplugin.setPluginCategory(handle, local_string(30022))  # Maintenance
	add_dir(local_string(30023),'',6,addon_icon,addon_fanart,local_string(30005),isFolder=False)  # Clear Packages
	add_dir(local_string(30024),'',7,addon_icon,addon_fanart,local_string(30008),isFolder=False)  # Clear Thumbnails
	add_dir(local_string(30025),'',8,addon_icon,addon_fanart,local_string(30009),isFolder=False)  # Advanced Settings
	add_dir(local_string(30026),'',10,addon_icon,addon_fanart,local_string(30026))  # Authorize Debrid Services

def authorize_menu():
    xbmcplugin.setPluginCategory(handle, local_string(30027))  # Authorize Services
    p = Parser(authorize)
    builds = json.loads(p.get_list())['items']
    for build in builds:
    	name = (build.get('name', 'Unknown'))
    	url = (build.get('url', ''))
    	icon = (build.get('icon', addon_icon))
    	fanart = (build.get('fanart', addon_fanart))
    	add_dir(name,url,2,icon,fanart,name,name2=name,version='' ,isFolder=False)