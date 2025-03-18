import os
import shutil


class Resolver:
    def __init__(self, parser, services_cls):
        self.parser = parser
        self.services_cls = services_cls


class AddResolver(Resolver):
    cmd = 'add'

    def run(self):
        for service in self.services_cls:
            if service.figure == self.parser.figure:
                service(self.parser).add()


class DeleteResolver(Resolver):
    cmd = 'delete'

    def run(self):
        for service in self.services_cls:
            if service.figure == self.parser.figure:
                service(self.parser).delete()


class ShowResolver(Resolver):
    cmd = 'show'

    def run(self):
        for service in self.services_cls:
            service(self.parser).show()


class DownloadResolver(Resolver):
    cmd = 'download'

    def run(self):
        shutil.copy("./tiny.db", self.parser.file_path)

