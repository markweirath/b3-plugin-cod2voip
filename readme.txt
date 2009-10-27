###################################################################################
#
# CoD2Voip
# Plugin for B3 (www.bigbrotherbot.com)
# (c) 2005 www.xlr8or.com (mailto:xlr8or@xlr8or.com)
#
# This program is free software and licensed under the terms of
# the GNU General Public License (GPL), version 2.
#
# http://www.gnu.org/copyleft/gpl.html
###################################################################################

CoD2Voip (v1.0.2) for B3
###################################################################################

This plugin works for CoD2 only! With this nifty little plugin you
can enable your admins to switch your VOIP settings. It adds 5 new
commands to B3:
 !voip <off, team, global> - switch teamchat, global chat or off
 !voipstatus - shows current status of your voip settings
 !voipquality <1-9> - Change soundquality settings
 !voipdead <on/off> - switch if dead ppl can talk to their teams
 !voipecho <on/off> - send a local echo to the clients

Each command can be leveled in the config file.


Requirements:
###################################################################################

- Call of Duty 2 server
- B3 version 1.1.0 or higher


Installation:
###################################################################################

1. Unzip the contents of this package into your B3 folder. It will
place the .py file in b3/extplugins and the config file .xml in
your b3/extplugins/conf folder.

2. Open the .xml file with your favorit editor and modify the
levels if you want them different. Do not edit the command-names
for they will not function under a different name.

3. Open your B3.xml file (in b3/conf) and add the next line in the
<plugins> section of the file:

<plugin name="cod2voip" priority="12" config="@b3/extplugins/conf/cod2voip.xml"/>

The numer 12 in this just an example. Make sure it fits your
plugin list.


Changelog
###################################################################################
v1.0.1 - v1.0.2: Using Cvar Class
                 'global' now turns deadchat on and 'team' turns it off
v1.0.0 - v1.0.1: Replaced console.set with console.setCvar
v1.0.0         : Initial release


###################################################################################
xlr8or - 1 dec 2005 - www.bigbrotherbot.com // www.xlr8or.com