function getPortNumber(defaultPort = 3000) {
  return process.env.PORT || defaultPort;
}

function isEnviromentSet(env = 'development') {
  return process.env.NODE_ENV === env;
}


module.exports = {
    getPortNumber,
    isEnviromentSet
};