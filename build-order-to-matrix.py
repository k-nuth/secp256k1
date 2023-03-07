import json

def main():
    matrix = {"include": []}

#     "config":
#         [
#             {"name": "Linux GCC 11",
#              "compiler": "GCC",
#              "version": "11",
#              "os": "ubuntu-20.04",
#              "docker_suffix": "-ubuntu16.04"
#             },

#             {"name": "macOS apple-clang 13","compiler": "apple-clang","version": "13","os": "macos-12"}]}



    with open("./ci_utils/.github/matrix.json", "r") as platform_file:
        platform_data = json.load(platform_file)

        with open("build_order.json", "r") as read_file:
            data = json.load(read_file)

            for level in data:
                for reference in level:
                    for platform in platform_data['config']:
                        platform["name"] = f'{platform["name"]} - {reference[0]}'
                        platform["reference"] = reference[0]
                        matrix["include"].append(platform)


            if len(matrix["include"]) == 0:
                matrix["include"].append({"reference": "null"})

    # print(matrix)
    with open("matrix.json", "w") as write_file:
        json.dump(matrix, write_file)

if __name__ == "__main__":
    main()
