$(document).ready(function() {
  
//LoadXML('XMLHolder','simple.xml');
if ($('#tree').length > 0)
{
  var filepath = 'test.xml'

  $(function() { 
      new XMLTree({fpath: filepath, container: '#tree', startExpanded: true,
      }); 
  
      //alert ($('ul[class="xmltree startExpanded"]').length)
      $('ul[class="xmltree startExpanded"]').prop('id','xmltree');
  });
      
  jQuery.expr[':'].Contains = function(a,i,m){
      return (a.textContent || a.innerText || "").toUpperCase().indexOf(m[3].toUpperCase())>=0;
  };

  //scroll to first child when filtering
  var container = $('body');
        
  $('#search_input').focus().keyup(function(e){
      var filter = $(this).val();
      if (filter) {
        $('#xmltree').find("li:not(:Contains(" + filter + "))").parent().hide();
        $('#xmltree').find("li:Contains(" + filter + ")").parent().show();
        $("#xmltree").find("li:Contains(" + filter + ")").children().show();
        $('#xmltree').highlight(filter);
        
        //scroll to first child when filtering
        var container = $('body');
        var scrollTo = $('#xmltree').children().find("li:Contains(" + filter + ")").first();
        
        console.log(scrollTo);
        container.scrollTop(
              scrollTo.offset().top - container.offset().top + container.scrollTop()
          );
        //scroll to first child when filtering- ends
      }
      else {
        container.offset().top = 0;
        $('#xmltree').find("li").children().slideDown();
        $('#xmltree').unhighlight();
      }
    });
    
    $('#search_input').focus().keydown(function(e){
        $('#xmltree').unhighlight();
    });
 }
});

jQuery.extend({
    highlight: function (node, re, nodeName, className) {
        if (node.nodeType === 3) {
            var match = node.data.match(re);
            if (match) {
                var highlight = document.createElement(nodeName || 'span');
                highlight.className = className || 'highlight';
                var wordNode = node.splitText(match.index);
                wordNode.splitText(match[0].length);
                var wordClone = wordNode.cloneNode(true);
                highlight.appendChild(wordClone);
                wordNode.parentNode.replaceChild(highlight, wordNode);
                return 1; //skip added node in parent
            }
        } else if ((node.nodeType === 1 && node.childNodes) && // only element nodes that have children
                !/(script|style)/i.test(node.tagName) && // ignore script and style nodes
                !(node.tagName === nodeName.toUpperCase() && node.className === className)) { // skip if already highlighted
            for (var i = 0; i < node.childNodes.length; i++) {
                i += jQuery.highlight(node.childNodes[i], re, nodeName, className);
            }
        }
        return 0;
    }
});

jQuery.fn.unhighlight = function (options) {
    var settings = { className: 'highlight', element: 'span' };
    jQuery.extend(settings, options);

    return this.find(settings.element + "." + settings.className).each(function () {
        var parent = this.parentNode;
        parent.replaceChild(this.firstChild, this);
        parent.normalize();
    }).end();
};


jQuery.fn.highlight = function (words, options) {
    var settings = { className: 'highlight', element: 'span', caseSensitive: false, wordsOnly: false };
    jQuery.extend(settings, options);
    
    if (words.constructor === String) {
        words = [words];
    }
    words = jQuery.grep(words, function(word, i){
      return word != '';
    });
    words = jQuery.map(words, function(word, i) {
      return word.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, "\\$&");
    });
    if (words.length == 0) { return this; };

    var flag = settings.caseSensitive ? "" : "i";
    var pattern = "(" + words.join("|") + ")";
    if (settings.wordsOnly) {
        pattern = "\\b" + pattern + "\\b";
    }
    var re = new RegExp(pattern, flag);
    
    return this.each(function () {
        jQuery.highlight(this, re, settings.element, settings.className);
    });
};