module.exports = function(RED) {
    function nodeFunction(config) {
        RED.nodes.createNode(this,config);
    }
    RED.nodes.registerType("OscTrig",nodeFunction);
}