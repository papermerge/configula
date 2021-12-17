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

Where ``papermerge.toml`` has following content:

    [ocr]
    default_language = 'deu'


    

    

