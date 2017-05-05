var Sequelize = require('sequelize');
module.exports = {'name':'bilan', 'define':{
    'uname': Sequelize.STRING(64),
    'upwd': Sequelize.STRING(64),
    'type': Sequelize.STRING(64),
    'isused': Sequelize.BOOLEAN,
  }
}
