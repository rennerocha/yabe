<div id="content">
%if post:
    <h1>{{ post.title }}</h1>
    <div id="post_content">
        {{ post.content }}
    </div>
%else:
    <h1>Nothing posted yet.</h1>
%end
</div>
<hr/>
<div id="comments">
  <form method="post" action="/new/comment/">
  <input type="hidden" name="post_id" value="{{post.id}}">
  <ul>
    <li><label for="author">Author</label><input type="text" name="author"></li>
    <li><textarea name="comment"></textarea></li>
  </ul>

  <input type="submit" value="Send Comment">
  </form>

%for comment in post.comments:
<hr/>
<p>{{ comment.author }}</p>
<p>{{ comment.comment }}</p>
%end
</div>

%rebase base page_title=page_title
