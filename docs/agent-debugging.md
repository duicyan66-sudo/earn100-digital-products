# Agent debugging

When an agent fails, do not immediately ask it to fix the fix. First find the first wrong assumption. Was the wrong file selected? Was a tool result partial? Did a test pass because it mocked the bug away?

The fastest recovery is usually smaller context, one failing command, and a prompt that asks for diagnosis before edits.
