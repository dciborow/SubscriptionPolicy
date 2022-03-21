from .cmdline import CmdUtils

class AzResourceGroup:

    @staticmethod
    def get_group(sub_id: str, group_name: str):
        return CmdUtils.get_command_output(
            [
                "az", 
                "group", 
                "show",
                "--name",
                group_name, 
                "--subscription", 
                sub_id
            ]
        )


    @staticmethod
    def get_groups(sub_id:str):
        return CmdUtils.get_command_output(
            [
                "az", 
                "group", 
                "list", 
                "--subscription", 
                sub_id
            ]
        )

    @staticmethod
    def delete_group(group_name:str, sub_id: str):
        print(f"Delete Resource Group: {group_name} in {sub_id}")
        CmdUtils.get_command_output(
            [
                "az",
                "group",
                "delete",
                "--name",
                group_name,
                "--subscription",
                sub_id,
                "--no-wait",
                "--yes"       
            ]
        )
