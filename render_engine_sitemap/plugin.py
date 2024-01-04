import logging
import pathlib

from jinja2.loaders import PackageLoader
from render_engine.plugins import hook_impl


class SiteMap:
    default_settings = {
        "output_path": "sitemap.xml",
        "map_item_pattern": "*.html",
    }

    @hook_impl
    def pre_build_site(
        site,
        settings: dict[str, any], 
    ) -> None:
        """
        Add the SiteMap template path to the theme manager.

        @hook_spec
        def pre_build_site(
            self,
            site,
            settings: dict[str, typing.Any],
        ) -> None:
        """
        site.theme_manager.prefix["SiteMap"] = PackageLoader(
            "render_engine_sitemap",
            "templates",
        )

    @hook_impl
    def post_build_site(
        site,
    ) -> None:
        """
        Generate a sitemap.xml file.

        parameters:
            site: The site object
        """
        plugin_settings = site.plugin_manager.plugin_settings["SiteMap"]
        logging.debug(
            f"Generating sitemap - {plugin_settings['output_path']} \
                from files matching - {plugin_settings['map_item_pattern']}"
        )
        template = site.theme_manager.engine.get_template("sitemap.xml")
        site_map_items = pathlib.Path(site.output_path).rglob(plugin_settings["map_item_pattern"])
        sitemap_path = pathlib.Path(site.output_path).joinpath(plugin_settings["output_path"])
        sitemap_path.write_text(
            template.render(
                items=[item.relative_to(site.output_path) for item in site_map_items],
            )
        )
