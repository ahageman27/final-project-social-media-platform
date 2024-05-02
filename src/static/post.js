$(document).ready(function() {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    // Function to fetch and display posts
    function fetchPosts() {
        $.get('/get_posts', function(data) {
            $('#postsArea').html(data);
        });
    }

    // Fetch posts on page load
    fetchPosts();

    // Handle form submission
    $('#postForm').submit(function(event) {
        event.preventDefault();
        var postContent = $('#postContent').val();
        socket.emit('new_post', { content: postContent });
        $('#postContent').val(''); // Clear the textarea
    });

    // SocketIO event handler for receiving new posts
    socket.on('new_post', function(data) {
        fetchPosts(); // Refresh posts
    });
});
