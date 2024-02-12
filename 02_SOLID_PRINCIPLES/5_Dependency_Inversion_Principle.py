''' 
The Dependency inversion Principle is a design principle that states the high-level
modules should not depend on low-level modules, but rather both should depend on abstractions.
This means that design of a system should depend on abstractions,rather than on concrete 
implementations.


To follow the Dependency inversion principle in your design:
    1. Identify the high-level and low-level modules in your system.The high-level
        modules are typically the ones that provide the overall functionality of the 
        system,while the low-level modules are the ones that provide the specific
        implementation details.
    2. Create abstractions for low-level modules.
    3. Have high-level modules depend on abstractions
    4. Have low-level modules implement abstractions.

'''

# Here is an example that violates Dependency inversion principle.

class FileSystem:
    def read_file(self,path):
        # code to read a file from the filesystem.
        pass
    def write_file(self,path,data):
        # code to write a file to the filesystem
        pass

class BackupService:
    def __init__(self):
        self.file_system = FileSystem()

    def backup(self,data):
        # code to generate a backup file name
        self.file_system.write_file(backup_file_name, data)


''' 
This example violates the Dependecy inversion principle because the BackupService class has
a direct dependency on the FileSystem class.This means that any changes to the FileSystem
class could potentially affect the BackupService class,and viceversa. This violates the
principle, as it means that the high-level Backupservice class depends on the
low-level FileSystem class.

To fix this issue and follow the DIP,we can introduce an abstraction for the fileSystem
fucntionality.Here's the refactored implementation.

'''

from abc import ABC, abstractmethod

class IFileSystem(ABC):
    @abstractmethod
    def read_file(self,path):
        pass

    @abstractmethod
    def write_file(self,path,data):
        pass


class FileSystem(IFileSystem):
    def read_file(self, path):
        pass

    def write_file((self, path, data):
        pass


class BackupService:
    def __init__(self,file_system: IFileSystem):
        self.file_system = file_system

    def backup(self,data):
        # code to generate a backup file name
        self.file_system.write_file(backup_file_name, data)


''' 
In this revised version of the system, the BackupService class depends on the
IFileSystem interface rather than on the FileSystem Class directly.This follows
the dependency inversion principle,as it ensures that the high-level BackupService
class does not depend on the low-level FileSystem class.

By introducing the abstraction, we have decoupled the BackupService class from
the FileSystem class,making the system more flexible and easier to modify. If we
need to change the way that the system reads and writes files,we can do so by modifying
the FileSystem class without affecting the BackupService class. This allows us to 
add new features or make changes to the system without causing unintended consequences. 

'''

