<form method="POST" action="/new/post">

<ul>
<li><label for="post_title">Author</label><input type="text" name="post_author"></li>
<li><label for="post_title">Title</label><input type="text" name="post_title"></li>
<li><label for="post_content">Content</label><textarea name="post_content"></textarea></li>
</ul>

<input type="submit" value="Send">
</form>

%rebase base page_title='New Post'
