
<div class="container">
  <div class="row">
    <h1>New Post</h1>
<form method="POST" action=".">

<ul class="unstyled">
<li><label for="post_title">Author</label><input type="text" name="post_author"></li>
<li><label for="post_title">Title</label><input type="text" name="post_title"></li>
<li><label for="post_content">Content</label><textarea name="post_content"></textarea></li>
</ul>

<input type="submit" value="Add new post">
</form>
  </div>
</div>

%rebase base page_title='New Post'
