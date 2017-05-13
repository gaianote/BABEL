const Sequelize = require('sequelize');

module.exports = {'name':'ip', 'define':{
    'ip': {
      'type':Sequelize.STRING(64),
    },
    'host':{
      'type':Sequelize.STRING(64),
      'unique':true,
    }
  }
}
