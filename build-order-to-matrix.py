import json

# V1:
# [ [ [ "gmp/6.2.1@#9cd6e4a851f6ffd6ea5b5d563f23abcc", "2189de39c5ef139630c496f152e2d3b4aec3412b", "host", "1" ] ] ]

# V2:
# {'ref': 'gmp/6.2.1#9cd6e4a851f6ffd6ea5b5d563f23abcc', 'depends': [], 'packages': [[{'package_id': '142664af885652f1b7b535d18ade2d1caa7142df', 'prev': '56d3269320f99a23fe632d47b2ad2acf', 'context': 'host', 'binary': 'Cache', 'options': ['*:march_id=ZLm9Pjh', '*:march_strategy=download_if_possible'], 'filenames': [], 'depends': []}]]}

# [
#     [
#         {
#             "ref": "gmp/6.2.1#9cd6e4a851f6ffd6ea5b5d563f23abcc",
#             "depends": [],
#             "packages": [
#                 [
#                     {
#                         "package_id": "142664af885652f1b7b535d18ade2d1caa7142df",
#                         "prev": "56d3269320f99a23fe632d47b2ad2acf",
#                         "context": "host",
#                         "binary": "Cache",
#                         "options": [
#                             "*:march_id=ZLm9Pjh",
#                             "*:march_strategy=download_if_possible"
#                         ],
#                         "filenames": [],
#                         "depends": []
#                     }
#                 ]
#             ]
#         }
#     ]
# ]

def main():
    matrix = {"include": []}

    with open("platform.json", "r") as platform_file:
        platform_data = json.load(platform_file)

        with open("build_order.json", "r") as read_file:
            data = json.load(read_file)
            # for level in data:
            #     for reference in level:
            #         print(reference["ref"])
            for level in data:
                for reference in level:
                    for platform in platform_data['config']:
                        # platform["name"] = f'{platform["name"]} - {reference[0]}'
                        # platform["reference"] = reference[0]

                        platform["name"] = f'{platform["name"]} - {reference["ref"]}'
                        platform["reference"] = reference["ref"]
                        matrix["include"].append(platform)


            if len(matrix["include"]) == 0:
                matrix["include"].append({"reference": "null"})

    # print(matrix)
    with open("matrix.json", "w") as write_file:
        json.dump(matrix, write_file)

if __name__ == "__main__":
    main()
