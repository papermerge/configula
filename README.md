# Configula

Creates a single configuration by merging multiple configuration
sources. It reads configurations from toml file and environment variables.
Values provided in environment variables have priority over values from 
toml configuration file.

## Installation

    $ poetry add configula

## Usage

    from configula import Configula
 
    configula = Configula(
        prefix='PAPERMERGE',
        config_locations=[
            'papermerge.toml',
            '/etc/papermerge.toml'
        ],
        config_env_var_name='PAPERMERGE_CONFIG'
    )
    
    # gets value from section 'ocr', variable 'default_language' 
    default_language = configula.get('ocr', 'default_language')
    port = configula.get_var('port')

Where ``papermerge.toml`` has the following content:

    port = 5432

    [ocr]
    default_language = 'deu'

Default language can be overwitten by environment
variable `PAPERMERGE_OCR_DEFAULT_LANGUAGE` and port can overwritten
by environment variable `PAPERMERGE_PORT`

If you want to read variable from a section use
`configula.get(section, var_name, default)` method.
If you want to read variable outside any section
use `configula.get_var(var_name, default)` method.

    

