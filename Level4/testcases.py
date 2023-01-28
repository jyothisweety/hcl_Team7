import pytest
from Level1.searchFile import FileFinder
from Level1.FindDrives import SystemDriveFinder
class Test_Drive:
    def test_DriveCase(self):
        obj=SystemDriveFinder()
        self.expected=obj.find_drives()
        self.actual=['C']
        assert self.expected==self.actual
    def test_searchfile(self):
        obj=FileFinder()
        d=obj.find_file('Sql file 1.txt','C:/')
        self.expected_filename=d[0]
        self.actual_res='C:/HCL1\\Sql file 1.txt'
        assert self.expected_filename==self.actual_res




