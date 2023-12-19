import typing
from render_engine.plugins import hook_impl

class class Renderenginesitemap:
    default_settings: {"default_setting": "default_value"}
    
    @hook_impl
    def post_build_site(
        self,
        site,
    ) -> None:
        """Build After Building the site"""
        pass
