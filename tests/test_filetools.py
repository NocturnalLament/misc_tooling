from src.misc_tooling.file_tools import (
    make_file,
    delete_file,
    write_file,
    delete_folder,
    file_exists,
)
import pytest
import os
import shutil
import pathlib
from pathlib import Path


class TestFileTools:
    def setup_method(self):
        self.folder = Path("test_stuff")
        self.folder.mkdir()

    def test_make_file(self):
        m = make_file("test_stuff/test.txt")
        exists = file_exists("test_stuff/test.txt")
        assert m
        assert exists
        if exists:
            delete_file("test_stuff/test.txt")

    def test_remove_file(self):
        m = make_file("test_stuff/test.txt")
        if m:
            delete_file("test_stuff/test.txt")
        exists = file_exists("test_stuff/test.txt")
        assert not exists

    def test_write_file(self):
        m = write_file("test_stuff/test.txt", "THIS IS A TEST")
        assert m

    def teardown_method(self):
        if self.folder.exists():
            for item in self.folder.iterdir():
                if item.is_file():
                    item.unlink()
        if not any(self.folder.iterdir()):
            self.folder.rmdir()
