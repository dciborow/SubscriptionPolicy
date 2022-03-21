from .cmdline import CmdUtils

class AzStorageUtil:
    @staticmethod
    def list_accounts(sub_id: str):
        command = f"az resource list --resource-type Microsoft.Storage/storageAccounts --subscription {sub_id}"


        return CmdUtils.get_command_output(command.split(' '))

    @staticmethod
    def get_account_details(sub_id, storage_acc, resource_group):
        command = f"az storage account show --name {storage_acc} --resource-group {resource_group} --subscription {sub_id}"


        return CmdUtils.get_command_output(command.split(' '))

    @staticmethod
    def is_blob_access_public(sub_id, storage_acc, resource_group):
        command = f"az storage account show --name {storage_acc} --resource-group {resource_group} --subscription {sub_id} --query allowBlobPublicAccess"


        value = CmdUtils.get_command_output(command.split(' '))

        # If there is no value then the default is enabled
        return_val = True
        if isinstance(value, bool):
            return_val = value
        elif isinstance(value, str):
            return_val = bool(value) if len(value) else True
        return return_val

    @staticmethod
    def disable_public_blob_access(sub_id, storage_acc, resource_group):
        command = f"az storage account update --name {storage_acc} --resource-group {resource_group} --subscription {sub_id} --allow-blob-public-access false --https-only true"


        CmdUtils.get_command_output(command.split(' '), False)

    @staticmethod
    def _enable_logging(connection_string, sub_id, services="bqt", logtype="rwd"):
        command = [
            "az", 
            "storage", 
            "logging", 
            "update", 
            "--log",
            logtype,
            "--retention",
            "10",
            "--services",
            services,
            "--connection-string",
            connection_string,
            "--subscription",
            sub_id
        ]
        CmdUtils.get_command_output(command)

    @staticmethod
    def enable_logging(sub_id, storage_acc, resource_group):
        command = f"az storage account show-connection-string -g {resource_group} -n {storage_acc} --subscription {sub_id}"


        output = CmdUtils.get_command_output(command.split(" "))

        if isinstance(output, dict):
            connection_string = output["connectionString"]
            AzStorageUtil._enable_logging(connection_string, sub_id)

