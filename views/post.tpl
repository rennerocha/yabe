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

%rebase base page_title=page_title
