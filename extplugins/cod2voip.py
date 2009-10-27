#
# CoD2Voip Plugin for BigBrotherBot(B3) (www.bigbrotherbot.com)
# Copyright (C) 2005 www.xlr8or.com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# Changelog:
# 1.0.0 - 1.0.1: Replaced console.set with console.setCvar, first one being depricated
# 1.0.1 - 1.0.2: Using Cvar class, global sets also deadchat on and team vice versa
#

__version__ = '1.0.2'
__author__  = 'xlr8or'

import b3, re
import b3.events

#--------------------------------------------------------------------------------------------------
class Cod2VoipPlugin(b3.plugin.Plugin):
  _adminPlugin = None

  def startup(self):
    """\
    Initialize plugin settings
    """

    # get the admin plugin so we can register commands
    self._adminPlugin = self.console.getPlugin('admin')
    if not self._adminPlugin:
      # something is wrong, can't start without admin plugin
      self.error('Could not find admin plugin')
      return False
    
    # register our commands
    if 'commands' in self.config.sections():
      for cmd in self.config.options('commands'):
        level = self.config.get('commands', cmd)
        sp = cmd.split('-')
        alias = None
        if len(sp) == 2:
          cmd, alias = sp

        func = self.getCmd(cmd)
        if func:
          self._adminPlugin.registerCommand(self, cmd, level, func, alias)

    self.debug('Started')


  def getCmd(self, cmd):
    cmd = 'cmd_%s' % cmd
    if hasattr(self, cmd):
      func = getattr(self, cmd)
      return func

    return None


  def handle(self, event):
    """\
    Handle intercepted events
    """


  def cmd_voipstatus(self, data, client, cmd=None):
    """\
    <status> - Check VOIP status.
    """

    # collect dvars from the server
    var_voice = self.console.getCvar('sv_voice').getInt()
    var_global = self.console.getCvar('voice_global').getInt()
    var_dead = self.console.getCvar('voice_deadChat').getInt()
    var_quality = self.console.getCvar('sv_voiceQuality').getInt()
    if var_dead == 1:
      var_deadchat = 'ON'
    elif var_dead == 0:
      var_deadchat = 'OFF'
    else:
      var_deadchat = 'NONE'        
    if var_voice == 0 and var_global == 0:
      var_voiceset = 'OFF'
    elif var_voice == 1 and var_global == 0:
      var_voiceset = 'TEAM'
    elif var_voice == 1 and var_global == 1:
      var_voiceset = 'GLOBAL'
    else:
      var_voiceset = 'NONE'
    # return the result to the client
    cmd.sayLoudOrPM(client, '^7VOIP ^1%s^7, deadchat ^1%s^7, quality ^1%s^7' % (var_voiceset, var_deadchat, var_quality))
    self.verbose('VOIPstatus checked by %s to "%s"', client.name, data)


  def cmd_voip(self, data, client, cmd=None):
    """\
    <off/team/global> - Set voip (voice over IP): ^1Off^7, to ^1Team Chat^7 or ^1Global Chat^7.
    """

    if data not in ('off','team','global'):
      client.message('Invalid option. Correct options are: off, team, global')
      return False

    if data == 'off':
      self.console.setCvar('sv_voice','0')
      self.console.setCvar('voice_global','0')
      self.console.say('^7VOIP switched ^1OFF^7')
    elif data == 'team':
      self.console.setCvar('sv_voice','1')
      self.console.setCvar('voice_global','0')
      self.console.setCvar('voice_deadChat','0')
      self.console.say('^7VOIP ^1Teamchat^7 Enabled, deadchat ^1OFF^7')
    elif data == 'global':
      self.console.setCvar('sv_voice','1')
      self.console.setCvar('voice_global','1')
      self.console.setCvar('voice_deadChat','1')
      self.console.say('^7VOIP ^1Global Chat^7 Enabled, deadchat ^1ON^7')

    self.verbose('VOIPsetting changed by %s to "%s"', client.name, data)

    
  def cmd_voipdead(self, data, client, cmd=None):
    """\
    <on/off> - Set voip (voice over IP) option DeadChat: Enable or Disable that dead ppl can talk to their team.
    """

    if data not in ('on','off'):
      client.message('Invalid option. Correct options are on or off')
      return False

    if data == 'on':
      self.console.setCvar('voice_deadChat','1')
      self.console.say('^7VOIP deadchat switched ^1ON^7')
    elif data == 'off':
      self.console.setCvar('voice_deadChat','0')
      self.console.say('^7VOIP deadchat switched ^1OFF^7')

    self.verbose('VOIP deadchat setting changed by %s to "%s"', client.name, data)


  def cmd_voipquality(self, data, client, cmd=None):
    """\
    <1 to 9> - Set voip (voice over IP) Quality setting.
    """
    
    m = re.match('^[1-9]$', data)
    if not m:
      client.message('Invalid option. Correct options are 1 to 9')
      return False
    else:
      self.console.setCvar('sv_voiceQuality', data)
      self.console.say('^7VOIP Quality set to ^1%s^7' % data)

    self.verbose('VOIP Quality setting changed by %s to "%s"', client.name, data)


  def cmd_voipecho(self, data, client, cmd=None):
    """\
    <on/off> - Set voip (voice over IP) option LocalEcho: Return sound to the speaker aswell?
    """

    if data not in ('on','off'):
      client.message('Invalid option. Correct options are on or off')
      return False

    if data == 'on':
      self.console.setCvar('voice_localEcho','1')
      self.console.say('^7VOIP Local Echo switched ^1ON^7')
    elif data == 'off':
      self.console.setCvar('voice_localEcho','0')
      self.console.say('^7VOIP Local Echo switched ^1OFF^7')

    self.verbose('VOIP local Echo setting changed by %s to "%s"', client.name, data)

if __name__ == '__main__':
  print '\nThis is version '+__version__+' by '+__author__+' for BigBrotherBot.\n'
