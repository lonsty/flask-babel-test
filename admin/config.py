# set optional bootswatch theme
# see http://bootswatch.com/3/ for available swatches

# FLASK_ADMIN_SWATCH = 'cerulean'
# FLASK_ADMIN_SWATCH = 'cosmo'
# FLASK_ADMIN_SWATCH = 'cyborg'
# FLASK_ADMIN_SWATCH = 'darkly' +
# FLASK_ADMIN_SWATCH = 'default'
# FLASK_ADMIN_SWATCH = 'flatly'
# FLASK_ADMIN_SWATCH = 'fonts'
# FLASK_ADMIN_SWATCH = 'journal'
# FLASK_ADMIN_SWATCH = 'lumen'
# FLASK_ADMIN_SWATCH = 'paper' ++
# FLASK_ADMIN_SWATCH = 'readable'
# FLASK_ADMIN_SWATCH = 'sandstone'
# FLASK_ADMIN_SWATCH = 'simplex'
# FLASK_ADMIN_SWATCH = 'slate'
# FLASK_ADMIN_SWATCH = 'spacelab'
# FLASK_ADMIN_SWATCH = 'superhero'
# FLASK_ADMIN_SWATCH = 'united' +
# FLASK_ADMIN_SWATCH = 'yeti'

# Create dummy secrey key so we can use sessions
SECRET_KEY = '123456790'

# Create in-memory database
DATABASE_FILE = 'sample_db.sqlite'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
