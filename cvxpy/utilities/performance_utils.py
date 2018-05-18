"""
Copyright 2017 Steven Diamond

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


def lazyprop(func):
    """Wraps a property so it is lazily evaluated.

    Args:
        func: The property to wrap.

    Returns:
        A property that only does computation the first time it is called.
    """
    attribute = '_comfy_{}'.format(func.__name__)

    @property
    def _comfyattr(self):
        """A lazily evaluated propery.
        """
        if not hasattr(self, attribute):
            setattr(self, attribute, func(self))
        return getattr(self, attribute)
    return _comfyattr
