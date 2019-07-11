# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-

from snapcraft.plugins.nodejs import NodePlugin


class ProdNodePlugin(NodePlugin):
    def run(self, cmd, rootdir):
        _cmd = str(cmd)
        if 'install' in _cmd and '--prod' not in _cmd:
            cmd.append('--production')
        if '--offline' in _cmd:
            cmd.remove('--offline')
        super().run(cmd, rootdir=rootdir)

    def run_output(self, cmd, rootdir):
        _cmd = str(cmd)
        if 'install' in _cmd and '--prod' not in _cmd:
            cmd.append('--production')
        if '--offline' in _cmd:
            cmd.remove('--offline')
        return super().run_output(cmd, rootdir=rootdir)
