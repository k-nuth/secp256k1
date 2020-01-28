import copy
import os
import cpuid
import platform
# from ci_utils import get_builder, handle_microarchs, copy_env_vars, filter_valid_exts, filter_marchs_tests
from kthbuild import get_base_march_ids, get_builder, handle_microarchs, copy_env_vars, filter_valid_exts, filter_marchs_tests

if __name__ == "__main__":
    full_build = os.getenv('KNUTH_FULL_BUILD', '0') == '1'

    builder, name = get_builder(os.path.dirname(os.path.abspath(__file__)))
    builder.add_common_builds(shared_option_name="%s:shared" % name, pure_c=True)

    filtered_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:

        if settings["build_type"] == "Release" \
                and not("%s:shared"  % name in options and options["%s:shared" % name]):

            copy_env_vars(env_vars)

            if os.getenv('KNUTH_RUN_TESTS', 'false') == 'true':
                # options["%s:with_benchmark" % name] = "True"
                options["%s:with_tests" % name] = "True"
                # options["%s:with_openssl_tests" % name] = "True"

            opts_no_schnorr = copy.deepcopy(options)
            opts_no_schnorr["%s:enable_module_schnorr" % name] = "False"

            # if full_build:
            #     marchs = filter_valid_exts(str(platform.system()), str(settings["compiler"]), float(str(settings["compiler.version"])), ['x86-64', 'haswell', 'skylake'])
            # else:
            #     marchs = ["x86-64"]
            # handle_microarchs("%s:microarchitecture" % name, marchs, filtered_builds, settings, options, env_vars, build_requires)
            # handle_microarchs("%s:microarchitecture" % name, marchs, filtered_builds, settings, opts_no_schnorr, env_vars, build_requires)

            march_ids = get_base_march_ids()
            handle_microarchs("%s:march_id" % name, march_ids, filtered_builds, settings, options, env_vars, build_requires)
            handle_microarchs("%s:march_id" % name, march_ids, filtered_builds, settings, opts_no_schnorr, env_vars, build_requires)

            filter_marchs_tests(name, filtered_builds, ["%s:with_tests" % name])

    builder.builds = filtered_builds
    builder.run()
