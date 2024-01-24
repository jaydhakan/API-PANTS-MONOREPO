python_requirement(
    name = 'app_requirements',
    requirements = [
        'uvicorn'
    ]
)

python_sources(
    name = 'app_config',
    sources = [
        'app_config.py'
    ]
)

pex_binary(
    name = 'app',
    dependencies = [
        ':app_config',
        ':app_requirements',
        'apps/auth:auth_app',
        'apps/platform:platform_app'
    ],
    entry_point = 'app.py',
    output_path = 'apps/main.pex'
)
