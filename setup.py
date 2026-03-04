from setuptools import setup, find_packages

setup(
    name="whiplash",
    version="1.0.0",
    author="tenn",
    description="Host servers within seconds.",
    long_description="Configuration. Servers. All yours -- in seconds.",
    long_description_content_type="text/plain",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "watchdog",
        "websockets",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "whiplash=whiplash.main:run"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
