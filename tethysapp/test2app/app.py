from tethys_sdk.base import TethysAppBase
# from tethys_sdk.app_settings import CustomSetting
from tethys_sdk.app_settings import CustomSimpleSetting


class Test2App(TethysAppBase):


    name = 'Test2App'
    description = ''
    package = 'test2app'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'test2app'
    color = '#2c3e50'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def custom_settings(self):
        """
        Example custom_settings method.
        """
        custom_settings = (

            # CustomSetting(
            #     name='default_name',
            #     type=CustomSetting.TYPE_STRING,
            #     description='Default model name.',
            #     required=True
            # ),
            # CustomSetting(
            #     name='max_count',
            #     type=CustomSetting.TYPE_INTEGER,
            #     description='Maximum allowed count in a method.',
            #     required=False
            # ),
            # CustomSetting(
            #     name='change_factor',
            #     type=CustomSetting.TYPE_FLOAT,
            #     description='Change factor that is applied to some process.',
            #     required=True
            # ),
            # CustomSetting(
            #     name='enable_feature',
            #     type=CustomSetting.TYPE_BOOLEAN,
            #     description='Enable this feature when True.',
            #     required=True
            # )
            CustomSimpleSetting(
                name='default_name',
                type=CustomSimpleSetting.TYPE_STRING,
                description='Default model name.',
                required=True
            ),
            CustomSimpleSetting(
                name='max_count',
                type=CustomSimpleSetting.TYPE_INTEGER,
                description='Maximum allowed count in a method.',
                required=False
            ),
            CustomSimpleSetting(
                name='change_factor',
                type=CustomSimpleSetting.TYPE_FLOAT,
                description='Change factor that is applied to some process.',
                required=True
            ),
            CustomSimpleSetting(
                name='enable_feature',
                type=CustomSimpleSetting.TYPE_BOOLEAN,
                description='Enable this feature when True.',
                required=True
            )
        )

        return custom_settings