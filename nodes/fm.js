module.exports = function(RED) {
    function nodeFunction(config) {
        RED.nodes.createNode(this,config);
        this.carrier = config.carrier;
    }
    RED.nodes.registerType("FM",nodeFunction);
}