const Sequelize = require('sequelize');

module.exports = {'name':'bilibili', 'define':{
    'uname': Sequelize.STRING(64),
    'upwd': Sequelize.STRING(64),
    'isused': Sequelize.BOOLEAN,
  }
}
